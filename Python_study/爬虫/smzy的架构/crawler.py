import aiohttp
import asyncio
import random
from datetime import datetime
from db_manager import DatabaseManager
from html_parser import HTMLParser

class Crawler:
    def __init__(self, db_manager, parser, semaphore, session, progress_bar, logger=None):
        self.db_manager = db_manager
        self.parser = parser
        self.semaphore = semaphore
        self.session = session
        self.progress_bar = progress_bar
        self.logger = logger or logging.getLogger(__name__)

    async def fetch_article_urls(self, base_url, num):
        article_urls = []
        tasks = [self.fetch_page_urls(base_url, i+1) for i in range(num)]
        results = await asyncio.gather(*tasks)
        for urls in results:
            article_urls.extend(urls)
        return article_urls

    async def fetch_page_urls(self, base_url, page_num):
        url = f"{base_url}/page/{page_num}"
        await asyncio.sleep(1)
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()  # 确保没有 HTTP 错误
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                return [a['href'] for a in soup.select('a.post-title')]
        except aiohttp.ClientError as e:
            self.logger.error(f"Error fetching page URLs: {url} - {e}")
            return []

    async def crawl(self, url, max_attempts=3):
        attempts = 0
        timeout = aiohttp.ClientTimeout(total=10)
        max_wait_time = 8  # 最大等待时间
        while attempts < max_attempts:
            async with self.semaphore:
                try:
                    async with self.session.get(url, allow_redirects=True, timeout=timeout) as response:
                        response.raise_for_status()  # 确保没有 HTTP 错误
                        html = await response.text()
                        data, error = self.parser.parse(html)
                        if data and not error:
                            try:
                                await self.db_manager.insert_data(data)
                                if self.progress_bar:
                                    self.progress_bar.update(1)
                            except ValueError as e:
                                self.logger.info(str(e))
                                return data, error  # 重复的文章，跳过并继续
                        return data, error
                except aiohttp.ClientError as e:
                    attempts += 1
                    wait_time = min(random.uniform(0.5, 1) + attempts, max_wait_time)
                    self.logger.warning(
                        f"Attempt {attempts} failed with client error: {e}. Retrying in {wait_time} seconds. URL: {url}")
                    await asyncio.sleep(wait_time)
                    continue
                except Exception as e:
                    self.logger.error(f"Error during crawling: {e}", exc_info=True)
                    return None, str(e)

        self.logger.error(f"Failed to retrieve {url} after {max_attempts} attempts")
        raise aiohttp.ClientError(f"Failed to retrieve {url} after {max_attempts} attempts")