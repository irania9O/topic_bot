from ..utils.db import database
from peewee import *
import datetime

class BaseModel(Model):
    class Meta:
        database = database

class TelegramUser(BaseModel):
    telegram_id = BigIntegerField(unique=True) 
    username = CharField(null=True) 
    first_name = CharField()
    last_name = CharField(null=True)
    language_code = CharField(max_length=10, default='en')
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)

database.connect()
database.create_tables([TelegramUser])

def add_user(telegram_id, username, first_name, last_name, language_code):
    user, created = TelegramUser.get_or_create(
        telegram_id=telegram_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'language_code': language_code,
            'is_active': True
        }
    )
    return user, created