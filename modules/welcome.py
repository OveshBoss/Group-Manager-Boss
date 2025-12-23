from pyrogram import filters
from bot import app

@app.on_message(filters.new_chat_members)
async def welcome(_, m):
    await m.reply(f"Welcome {', '.join([u.mention for u in m.new_chat_members])}!")
