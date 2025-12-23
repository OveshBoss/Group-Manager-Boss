from pyrogram import Client, filters
from config import *
import help_menu

# Import modules
from modules import fsub, bans, warnings, locks, welcome, rules, connections
from modules import filters as filters_module  # rename import to avoid conflict

# Initialize bot client
app = Client("mega_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize all modules with app
fsub.init(app)
bans.init(app)
warnings.init(app)
filters_module.init(app)
locks.init(app)
welcome.init(app)
rules.init(app)
connections.init(app)

# Start command
@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply(
        "**ʜᴇʏ 👋**\n**ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴇɢᴀ ɢʀᴏᴜᴘ ʙᴏᴛ**",
        reply_markup=help_menu.start_buttons()
    )

print("Bot started successfully")
app.run()
