import datetime
from peewee import (
    SqliteDatabase,
    Model,
    IntegerField,
    CharField,
    DateField,
    BooleanField,
)
from typing import Optional
from core.config import DATABASE_NAME


# Подключение к базе данных
db = SqliteDatabase(DATABASE_NAME)


# Определение базовой модели
class BaseModel(Model):
    class Meta:
        database = db


class Src(BaseModel):
    file_name = CharField(unique=True)
    file_id = CharField(default="")


class SrcDatabase:
    def __init__(self, db_name=DATABASE_NAME):
        self.db = SqliteDatabase(db_name)
        self.create_table()

    def create_table(self):
        self.db.connect()
        self.db.create_tables([Src])

    def create_src(self, file_name: str):
        try:
            Src.create(file_name=file_name)
            return None
        except Exception:

            return Src.get(Src.file_name == file_name)

    def update_src(self, file_name: str, file_id: str):
        try:
            src = Src.get(Src.file_name == file_name)
            src.file_id = file_id
            src.save()
        except Exception:
            pass
