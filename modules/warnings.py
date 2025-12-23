from pyrogram import filters

def init(app):
    @app.on_message(filters.command("warn") & filters.admin)
    async def warn(_, m):
        await m.reply("Warn logic placeholder")
