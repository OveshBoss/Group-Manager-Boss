from pyrogram import filters

def init(app):
    @app.on_message(filters.command("rules") & filters.admin)
    async def rules_cmd(_, m):
        await m.reply("Rules placeholder")
