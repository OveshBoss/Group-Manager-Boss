from pyrogram import Client
from config import *
import help_menu

# import modules
from modules import fsub, bans, warnings, filters_module, locks, welcome, rules, connections

app = Client("mega_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# initialize all modules with app
fsub.init(app)
bans.init(app)
warnings.init(app)
filters_module.init(app)
locks.init(app)
welcome.init(app)
rules.init(app)
connections.init(app)

# start command
from pyrogram import filters

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply(
        "**ʜᴇʏ 👋**\n**ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴇɢᴀ ɢʀᴏᴜᴘ ʙᴏᴛ**",
        reply_markup=help_menu.start_buttons()
    )

print("Bot started successfully")
app.run()
