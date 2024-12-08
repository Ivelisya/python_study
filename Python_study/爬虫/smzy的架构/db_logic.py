import asyncio
import logging

from tortoise import Tortoise
from aiohttp import TCPConnector
from db_manager import DatabaseManager
from html_parser import HTMLParser


async def init_orm(db_config, logger=None):
    try:
        async with Tortoise.init(
                db_url=db_config['db_url'],
                modules={'models': ['models']}
        ):
            await Tortoise.generate_schemas()
    except Exception as e:
        logger.error(f"Error initializing ORM: {e}", exc_info=True)
        raise


async def fetch_and_crawl(base_url, num, concurrency, config_path='config.yaml', logger=None):
    config = load_config(config_path)
    logger = logger or setup_logging(config.get('logging_config_path', 'logging_config.yaml'))

    try:
        logger.info(f"开始从 {base_url} 爬取文章.")

        await init_orm(config['database'], logger=logger)
        semaphore_limit = concurrency or config['semaphore_limit']
        connector = TCPConnector(limit=semaphore_limit)

        async with aiohttp.ClientSession(connector=connector) as session:
            db_manager = DatabaseManager(logger=logger)
            parser = HTMLParser()
            progress_bar = click.progressbar(length=num, show_pos=True, label='爬取进度')
            crawler = Crawler(db_manager, parser, asyncio.Semaphore(semaphore_limit), session, progress_bar,
                              logger=logger)

            article_urls = await crawler.fetch_article_urls(base_url, num)

            with progress_bar:
                tasks = [crawler.crawl(url) for url in article_urls]
                await asyncio.gather(*tasks)

            logger.info(f"完成爬取 {len(article_urls)} 篇文章.")
    except Exception as e:
        logger.error(f"Error in fetch_and_crawl: {e}", exc_info=True)
    finally:
        await Tortoise.close_connections()