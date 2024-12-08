from datetime import datetime
from dateutil.parser import parse
from bs4 import BeautifulSoup

class HTMLParser:
    def parse(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.get_text(strip=True) if soup.title else 'Unknown'
            author = soup.select_one('a[itemprop="author"]').get_text(strip=True) if soup.select_one(
                'a[itemprop="author"]') else 'Unknown'
            created_at_str = soup.select_one('time[itemprop="datePublished"]').get_text(
                strip=True) if soup.select_one('time[itemprop="datePublished"]') else None

            created_at = datetime.utcnow() if created_at_str is None else parse(created_at_str)

            content = ''.join(
                [str(p) for p in soup.select_one('div.entry-content').find_all('p')]) if soup.select_one(
                'div.entry-content') else ''

            data = {
                'title': title,
                'author': author,
                'created_at': created_at,
                'content': content
            }
            return data, None
        except Exception as e:
            self.logger.error(f"Error parsing HTML: {e}", exc_info=True)
            raise  # 抛出异常以便更好地处理错误