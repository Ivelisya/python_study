import asyncio
import aiomysql
import aiohttp
from bs4 import BeautifulSoup
import logging.config
import yaml
import click
import os

# ...其他函数和类的定义...

@click.group()
def cli():
    pass

@cli.command(help='Run the crawler in standard mode.')
@click.argument('urls', nargs=-1)
@click.option('--log-level', default='INFO', show_default=True, help='Set the logging level.')
@click.option('--log-file', default='crawler.log', show_default=True, help='Set the logging file path.')
def standard(urls, log_level, log_file):
    setup_env(log_level, log_file)
    setup_logging()
    asyncio.run(run_crawler(urls, mode='standard'))

@cli.command(help='Run the crawler in performance mode.')
@click.argument('urls', nargs=-1)
@click.option('--concurrency', default=50, show_default=True, help='Set the concurrency level for performance mode.')
def performance(urls, concurrency):
    setup_env('CRITICAL', 'performance.log')
    setup_logging()
    asyncio.run(run_crawler(urls, mode='performance', concurrency=concurrency))

def setup_env(log_level, log_file):
    os.environ['CRAWLER_LOG_LEVEL'] = log_level
    os.environ['CRAWLER_LOG_FILE'] = log_file

async def run_crawler(urls, mode='standard', concurrency=10):
    app_config = open_yaml_file('config.yaml')
    db_manager = DatabaseManager(app_config['database'])
    await db_manager.create_pool()
    try:
        parser = HTMLParser()
        semaphore_limit = concurrency if mode == 'performance' else app_config['semaphore_limit']
        semaphore = asyncio.Semaphore(semaphore_limit)
        crawler = Crawler(db_manager, parser, semaphore, app_config['headers'])
        await crawler.start_session()

        # 分批处理URLs
        tasks = []
        for url in urls:
            task = asyncio.create_task(safe_run(crawler, url))
            tasks.append(task)
            if len(tasks) >= concurrency:
                await asyncio.gather(*tasks)
                tasks = []

        # 确保最后一批任务也被执行
        if tasks:
            await asyncio.gather(*tasks)

    finally:
        await crawler.close_session()
        await db_manager.close_pool()

if __name__ == '__main__':
    cli()