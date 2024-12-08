import asyncio
import logging.config
import os
from datetime import datetime
from dateutil.parser import parse
import random
import aiohttp
from aiohttp import TCPConnector
from bs4 import BeautifulSoup
from tortoise import Tortoise, fields, exceptions
from tortoise.models import Model
import yaml
import asyncclick as click

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = {
    'db_url': 'sqlite://:memory:',
    'logging_config_path': 'logging_config.yaml',
    'database': 'default',
    'semaphore_limit': 50,
    'db_config': {
        'minsize': 1,
        'maxsize': 10,
        # Add other database configuration parameters
    }
}
logger = logging.getLogger(__name__)

class ConfigurationError(Exception):
    pass

class ConfigurationManager:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(SCRIPT_DIR, self.config_path)
        config_data = DEFAULT_CONFIG
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f) or DEFAULT_CONFIG
                if not all(key in config_data for key in ['db_url', 'logging_config_path', 'database', 'semaphore_limit']):
                    raise ConfigurationError("Configuration is missing required keys.")
            else:
                raise FileNotFoundError(f"Config file not found: {config_path}")
        except yaml.YAMLError as e:
            raise ConfigurationError(f"Error loading configuration: {e}")
        except Exception as e:
            raise ConfigurationError(f"Error loading configuration: {e}")
        return config_data

    def get_config(self):
        return self.config

def setup_logging(log_config_path='logging_config.yaml', default_level=logging.INFO):
    config_path = os.path.join(SCRIPT_DIR, log_config_path)
    try:
        if os.path.exists(config_path):
            with open(config_path, 'rt', encoding='utf-8') as f:
                log_config = yaml.safe_load(f.read())
                if not log_config:
                    raise ConfigurationError("Empty or invalid logging configuration.")
            logging.config.dictConfig(log_config)
        else:
            logging.basicConfig(
                level=default_level,
                format="%(asctime)s - %(levelname)s - %(message)s",
            )
            logger.debug(f"Config file '{config_path}' not found. Using default logging level.")
    except yaml.YAMLError as e:
        logging.basicConfig(
            level=default_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logger.error(f"Error loading logging configuration: {e}")
    except Exception as e:
        logging.basicConfig(
            level=default_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logger.error(f"Error setting up logging: {e}")

class ParsingError(Exception):
    pass

class HTMLParser:
    def __init__(self, config):
        self.config = config

    def parse(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title_selector = self.config.get('title_selector', 'title')
            author_selector = self.config.get('author_selector', 'a[itemprop="author"]')
            created_at_selector = self.config.get('created_at_selector', 'time[itemprop="datePublished"]')

            title = soup.select_one(title_selector).get_text(strip=True) if soup.select_one(title_selector) else 'Unknown'
            author = soup.select_one(author_selector).get_text(strip=True) if soup.select_one(author_selector) else 'Unknown'
            created_at_str = soup.select_one(created_at_selector).get_text(strip=True) if soup.select_one(created_at_selector) else None

            created_at = datetime.utcnow() if created_at_str is None else parse(created_at_str)

            content_selector = self.config.get('content_selector', 'div.entry-content')
            content = ''.join([str(p) for p in soup.select_one(content_selector).find_all('p')]) if soup.select_one(content_selector) else ''

            data = {
                'title': title,
                'author': author,
                'created_at': created_at,
                'content': content
            }
            return data, None
        except (AttributeError, TypeError) as ae:
            error_msg = f"Error during HTML parsing: {ae}"
            logger.error(error_msg, exc_info=True)
            raise ParsingError(error_msg)
        except Exception as e:
            error_msg = f"Error during HTML parsing: {e}"
            logger.error(error_msg, exc_info=True)
            raise ParsingError(error_msg)

class DataInsertionError(Exception):
    pass

class Article(Model):
    title = fields.TextField()
    author = fields.TextField()
    created_at = fields.DatetimeField()
    content = fields.TextField()

class DatabaseManager:
    async def insert_data(self, data):
        try:
            article, created = await Article.get_or_create(**data)
            if created:
                logger.info(f"Article '{data['title']}' by {data['author']} inserted.")
            else:
                logger.info(f"Article '{data['title']}' by {data['author']} already exists. Skipping insertion.")
        except exceptions.TortoiseError as te:
            error_msg = f"TortoiseError during data insertion: {te}"
            logger.error(error_msg, exc_info=True)
            raise DataInsertionError(error_msg)
        except Exception as e:
            error_msg = f"Error during data insertion: {e}"
            logger.error(error_msg, exc_info=True)
            raise DataInsertionError(error_msg)

class Crawler:
    def __init__(self, db_manager, parser, semaphore, session):
        self.db_manager = db_manager
        self.parser = parser
        self.semaphore = semaphore
        self.session = session

    async def fetch_article_urls(self, base_url, num):
        logger.info(f"开始从 {base_url} 获取文章URLs")
        article_urls = []
        for i in range(num):
            page_urls = await self.fetch_page_urls(base_url, i + 1)
            article_urls.extend(page_urls)
            logger.info(f"从 {base_url}/page/{i+1} 获取了 {len(page_urls)} 个URLs")
        logger.info(f"总共获取了 {len(article_urls)} 个文章URLs")
        return article_urls

    async def fetch_page_urls(self, base_url, page):
        url = f"{base_url}/page/{page}"
        logger.info(f"正在获取页面: {url}")
        async with self.session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                urls = [a['href'] for a in soup.select('a.post-title')]
                logger.info(f"从页面 {url} 获取了 {len(urls)} 个文章URLs")
                return urls
            else:
                logger.warning(f"无法获取 {url}: HTTP状态码 {response.status}")
                return []

    async def crawl(self, url, max_attempts=3):
        logger.info(f"开始爬取文章: {url}")
        async with self.semaphore:
            for attempt in range(max_attempts):
                try:
                    async with self.session.get(url) as response:
                        if response.status == 200:
                            html = await response.text()
                            article_data, _ = self.parser.parse(html)
                            await self.db_manager.insert_data(article_data)
                            logger.info(f"成功爬取并存储文章: {url}")
                            break
                        else:
                            logger.warning(f"尝试 {attempt+1}/{max_attempts} 失败: {url} 返回了状态码 {response.status}")
                except aiohttp.ClientError as e:
                    logger.warning(f"尝试 {attempt+1}/{max_attempts} 失败: {e}")
                    if attempt == max_attempts - 1:
                        logger.error(f"达到最大尝试次数，无法爬取: {url}")
                except Exception as e:
                    logger.error(f"爬取过程中出现异常: {e}")

                await asyncio.sleep(random.uniform(0.5, 1))  # 稍微等待，然后重试

@click.group()
@click.pass_context
@click.option('--config', help='Path to the configuration file.', default='config.yaml')
def cli(ctx, config):
    config_manager = ConfigurationManager(config)
    ctx.obj = {
        'config_manager': config_manager,
        'config': config_manager.get_config()
    }
    setup_logging(ctx.obj['config'].get('logging_config_path', 'logging_config.yaml'))

@cli.command(help="Fetch and crawl articles from a base URL.")
@click.argument('base_url')
@click.argument('num', type=int)
@click.argument('concurrency', type=int)
@click.pass_context
async def fetch_and_crawl(ctx, base_url, num, concurrency):
    config = ctx.obj['config']
    db_manager = DatabaseManager()
    parser = HTMLParser(config)

    logger.info("Initializing database")
    await Tortoise.init(
        db_url=config['db_url'],
        modules={'models': [__name__]},
        **config.get('db_config', {})
    )
    await Tortoise.generate_schemas()
    logger.info(f"Database initialized")

    logger.info(f"开始从 {base_url} 爬取文章")
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        semaphore = asyncio.Semaphore(concurrency)
        crawler = Crawler(db_manager, parser, semaphore, session)
        article_urls = await crawler.fetch_article_urls(base_url, num)

        tasks = [crawler.crawl(url) for url in article_urls]
        await asyncio.gather(*tasks)
        logger.info(f"完成爬取 {len(article_urls)} 篇文章")

    logger.info("Closing database connection")
    await Tortoise.close_connections()

if __name__ == "__main__":
    cli(_anyio_backend="asyncio")
