from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me", url="https://t.me/YOUR_BOT_USERNAME?startgroup=true")],
        [InlineKeyboardButton("👑 Owner", url="https://t.me/user?id=1416433622"),
         InlineKeyboardButton("📢 Channel", url="https://t.me/OnlyBossMoviesGroup")]
    ])
