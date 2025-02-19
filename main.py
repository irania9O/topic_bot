import asyncio
import logging
import sys
from utils.settings import PROXY, BOT_TOKEN
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


registered_topics = {}

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

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
async def message_checker(message: Message) -> None:
    try:
        if message.message_thread_id in registered_topics:
            if message.from_user.id != registered_topics[message.message_thread_id]["owner"]:
                if registered_topics[message.message_thread_id]["is_locked"]:
                    await message.delete()
    except TypeError:
        await message.answer("Oops!")


async def main() -> None:
    session = AiohttpSession(proxy=PROXY)
    bot = Bot(token=BOT_TOKEN, session=session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())