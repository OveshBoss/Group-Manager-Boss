from pyrogram import filters

def init(app):
    @app.on_message(filters.command("ban") & filters.admin)
    async def ban(_, m):
        if m.reply_to_message:
            await app.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
            await m.reply("User banned ✅")
