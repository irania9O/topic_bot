from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from db.user import add_user

class UserCreatorMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        add_user(Message.from_user.id, Message.from_user.username, Message.from_user.first_name, Message.from_user.last_name,  Message.from_user.language_code)
        return await handler(event, data)