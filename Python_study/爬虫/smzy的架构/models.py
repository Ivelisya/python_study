from tortoise import Tortoise, fields, exceptions
from tortoise.models import Model

class Article(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    content = fields.TextField()

    class Meta:
        table = "articles"

# db_manager.py

import logging
from tortoise.exceptions import TortoiseError

class DatabaseManager:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    async def insert_data(self, data):
        try:
            article, created = await Article.get_or_create(**data)
            if created:
                self.logger.info(f"Article '{data['title']}' by {data['author']} inserted.")
            else:
                self.logger.info(f"Article '{data['title']}' by {data['author']} already exists. Skipping insertion.")
        except TortoiseError as e:
            self.logger.error(f"Error inserting data into the database: {e}", exc_info=True)
            raise  # 抛出异常以便更好地处理错误