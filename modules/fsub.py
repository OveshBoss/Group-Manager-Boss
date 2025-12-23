from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import fsub

def init(app):

    @app.on_message(filters.command("set_fsub") & filters.admin)
    async def set_fsub(_, m):
        if len(m.command) != 2:
            return await m.reply("Use: /set_fsub -100CHANNELID")
        fsub.update_one(
            {"chat": m.chat.id},
            {"$set": {"channel": int(m.command[1])}},
            upsert=True
        )
        await m.reply("Force Subscribe Enabled ✅")

    @app.on_message(filters.command("remove_fsub") & filters.admin)
    async def remove_fsub(_, m):
        fsub.delete_one({"chat": m.chat.id})
        await m.reply("Force Subscribe Removed ❌")

    @app.on_message(filters.group & ~filters.service)
    async def enforce_fsub(_, m):
        data = fsub.find_one({"chat": m.chat.id})
        if not data:
            return
        try:
            await app.get_chat_member(data["channel"], m.from_user.id)
        except:
            await m.delete()
            await m.reply(
                "🚫 You must join the channel first!",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/c/{str(data['channel'])[4:]}")]]
                )
            )
