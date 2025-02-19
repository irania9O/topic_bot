import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dotenv import load_dotenv
load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

registered_topics = {}

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(Command("register"))
async def register_topic(message: Message):
    if message.reply_to_message is None:
            await message.answer(f"You should reply to a message with a topic to register it to a user")
            return
    
    if message.message_thread_id is None:
        await message.answer("This message does not have a topic, so it can't be registered")
        return
        


    registered_topics[message.reply_to_message.message_thread_id] = {
        "id": message.message_thread_id,
        "owner": message.reply_to_message.from_user.id,
        "is_locked": False
    }
    await message.answer(f"Topic registered to user {message.reply_to_message.from_user.full_name}")


@dp.message(Command("lock_door"))
async def lock_door(message: Message):
    if message.message_thread_id in registered_topics:
        if message.from_user.id == registered_topics[message.message_thread_id]["owner"]:
            registered_topics[message.message_thread_id]["is_locked"] = True
            await message.answer("Door is locked")
        else:
            await message.answer("You are not the owner of this topic")
    else:
        await message.answer("This topic is not registered")

@dp.message(Command("unlock_door"))
async def unlock_door(message: Message):
    if message.message_thread_id in registered_topics:
        if message.from_user.id == registered_topics[message.message_thread_id]["owner"]:
            registered_topics[message.message_thread_id]["is_locked"] = False
            await message.answer("Door is unlocked")
        else:
            await message.answer("You are not the owner of this topic")
    else:
        await message.answer("This topic is not registered")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        # await message.send_copy(chat_id=message.chat.id)
        if message.message_thread_id in registered_topics:
            if message.from_user.id != registered_topics[message.message_thread_id]["owner"]:
                if registered_topics[message.message_thread_id]["is_locked"]:
                    await message.delete()
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    session = AiohttpSession(proxy="socks5://127.0.0.1:2080")

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, session=session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())