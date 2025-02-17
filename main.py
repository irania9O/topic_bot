from pyrogram import Client, filters
from settings import proxy

app = Client("my_account", proxy=proxy)



@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()