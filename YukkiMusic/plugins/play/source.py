import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس مين","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/music_rio_bot",
        caption=f"""[◍ 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒔𝒐𝒖𝒓𝒄𝒆 𝒌𝒂𝒓𝒎𝒂𝒏 √🖥](https://t.me/YDDCJ)\n\n[◍ 𝒕𝒉𝒆 𝒃𝒆𝒔𝒕 𝒔𝒐𝒖𝒓𝒄𝒆 𝒐𝒏 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 √🌐](https://t.me/YDDCJ)\n\n[◍ 𝒇𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒃𝒆𝒍𝒐𝒘 √🔮](https://t.me/YDDCJ)\n\n||[◍ #،𝙑𝒗 𝙄𝒊 𝙍𝒓 𝙐𝒖 𝙎𝒔 💎⛓ √](https://t.me/VR_LA)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 𝗩𝗜𝗥𝗨𝗦 』", url=f"https://t.me/VR_LA"), 
                ],[
                    InlineKeyboardButton(
                        "『 𝗦𝗢𝗨𝗥𝗖𝗘 𝗞𝗔𝗥𝗠𝗔𝗡 』", url=f"https://t.me/YDDCJ"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/music_rio_bot?startgroup=true"),
                ],

            ]

        ),

    )
