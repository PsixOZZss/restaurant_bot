from aiogram.filters import BaseFilter
from aiogram.types import Message

# from filters.admin_filter import ADMIN_LIST


class UserFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        # return message.from_user.id not in ADMIN_LIST
        return True
