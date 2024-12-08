import asyncio
import click
import logging
import logging.config
import yaml
from aiohttp import ClientSession, TCPConnector
from tortoise import Tortoise

from config_manager import ConfigurationManager
from database_manager import DatabaseManager
from html_parser import HTMLParser
from crawler import Crawler

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)

async def init_orm(config):
    db_url = config.get('db_url', 'sqlite://:memory:')
    try:
        await Tortoise.init(
            db_url=db_url,
            modules={'models': ['database_manager']}
        )
        await Tortoise.generate_schemas()
    except Tortoise.exceptions.TortoiseError as e:
        logger.error(f"Error initializing ORM: {e}", exc_info=True)
        raise

def setup_logging(log_config_path='logging_config.yaml', default_level=logging.INFO):
    config_path = os.path.join(SCRIPT_DIR, log_config_path)

    if os.path.exists(config_path):
        with open(config_path, 'rt', encoding='utf-8') as f:
            log_config = yaml.safe_load(f.read())
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(
            level=default_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logger.debug(f"Config file '{config_path}' not found. Using default logging level.")

    return logger

@click.group()
def cli():
    pass

@cli.command(help="Fetch and crawl articles from a base URL.")
@click.argument('base_url', type=str, metavar='BASE_URL', required=True)
@click.argument('num', type=int, metavar='NUM', required=True)
@click.option('--concurrency', type=int, required=True, show_default=True,
              help='Set the concurrency level for fetching and crawling.')
@click.option('--config', default='config.yaml', show_default=True, help='Path to the configuration file.')
async def fetch_and_crawl(base_url, num, concurrency, config):
    config_manager = ConfigurationManager(config)
    config_data = config_manager.get_config()
    logger = setup_logging(config_data.get('logging_config_path', 'logging_config.yaml'))

    try:
        logger.info(f"开始从 {base_url} 爬取文章.")
        await init_orm(config_data)
        semaphore_limit = concurrency or config_data.get('semaphore_limit', 10)
        async with ClientSession(connector=TCPConnector(limit=semaphore_limit)) as session:
            db_manager = DatabaseManager()
            parser = HTMLParser()
            progress_bar = None  # 如果需要进度条，可以在这里实现
            crawler = Crawler(db_manager, parser, asyncio.Semaphore(semaphore_limit), session, progress_bar)
            article_urls = await crawler.fetch_article_urls(base_url, num)
            if article_urls:
                tasks = [crawler.crawl(url) for url in article_urls]
                await asyncio.gather(*tasks)
            logger.info(f"完成爬取 {len(article_urls)} 篇文章.")
    except Exception as e:
        logger.error(f"Error in fetch_and_crawl: {e}", exc_info=True)
    finally:
        await Tortoise.close_connections()

if __name__ == '__main__':
    asyncio.run(cli())