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


# Модель пользователя
class User(BaseModel):
    user_id = IntegerField(unique=True)
    date_registration = DateField(default=datetime.date.today)
    name = CharField(default="")
    phone_number = CharField(default="")


class UserDatabase:
    def __init__(self, db_name=DATABASE_NAME):
        # Инициализация базы данных
        self.db = SqliteDatabase(db_name)
        self.create_table()

    def create_table(self):
        # Создание таблицы, если она не существует
        self.db.connect()
        self.db.create_tables([User])

    def create_user(self, user_id: int):
        # Добавление пользователя в базу данных
        try:
            User.create(user_id=user_id)
        except Exception:
            # Если пользователь уже существует (например, нарушение уникальности),
            # исключение будет проигнорировано
            pass

    def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
    ):
        # Добавление пользователя в базу данных
        try:
            user = User.get(User.user_id == user_id)

            if phone_number:
                user.phone_number = phone_number

            if name:
                user.name = name

            user.save()
        except Exception:
            # Если пользователь уже существует (например, нарушение уникальности),
            # исключение будет проигнорировано
            pass

    def read_user(
        self,
        user_id: int,
    ):
        # Добавление пользователя в базу данных
        try:
            return User.get(User.user_id == user_id)
        except Exception:
            # Если пользователь уже существует (например, нарушение уникальности),
            # исключение будет проигнорировано
            pass
