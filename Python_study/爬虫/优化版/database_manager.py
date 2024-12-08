# database_manager.py
import logging
from tortoise import Tortoise, fields, exceptions
from models import Article

logger = logging.getLogger(__name__)

class DatabaseManager:
    async def insert_data(self, data):
        try:
            article, created = await Article.get_or_create(**data)
            if created:
                logger.info(f"Article '{data['title']}' by {data['author']} inserted.")
            else:
                logger.info(f"Article '{data['title']}' by {data['author']} already exists. Skipping insertion.")
        except exceptions.TortoiseError as e:
            logger.error(f"Error inserting data into the database: {e}", exc_info=True)
            raise  # 抛出异常以便更好地处理错误