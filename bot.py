from pyrogram import Client, filters
from config import *
# Import modules
import modules.fsub
import modules.bans
import modules.warnings
import modules.filters
import modules.locks
import modules.welcome
import modules.rules
import modules.connections
import help_menu

app = Client(
    "mega_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply(
        "**ʜᴇʏ 👋**\n**ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴇɢᴀ ɢʀᴏᴜᴘ ʙᴏᴛ**",
        reply_markup=help_menu.start_buttons()
    )

print("bot started successfully")
app.run()
