from pyrogram import filters

def init(app):
    @app.on_message(filters.command("lock") & filters.admin)
    async def lock_cmd(_, m):
        await m.reply("Lock logic placeholder")
