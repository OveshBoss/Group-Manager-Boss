from pyrogram import filters

def init(app):
    @app.on_message(filters.command("connect") & filters.admin)
    async def connect_cmd(_, m):
        await m.reply("Connect placeholder")
