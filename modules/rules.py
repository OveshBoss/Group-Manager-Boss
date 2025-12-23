from pyrogram import filters
from bot import app

@app.on_message(filters.command("rules") & filters.admin)
async def rules_cmd(_, m):
    await m.reply("Rules placeholder")
