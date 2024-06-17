import random
from pyrogram import filters
from Mitsuri import app
from Mitsuri import *
from ... import *
import config

from ...logging import LOGGER

from Mitsuri import app, userbot
from Mitsuri.core.userbot import *

import asyncio

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
from Mitsuri.core.userbot import Userbot
from datetime import datetime

# Assuming Userbot is defined elsewhere
userbot = Userbot()


BOT_LIST = ["Mitsuri_Robot", "DazaiProBot", "Cha_Hae_In_Bot ", "Sung_Jin_Woo_Bot", "Shinobu_Bot"]

@app.on_message(filters.command("botschk") & filters.user(OWNER_ID))
async def bots_chk(_, message):
    msg = await message.reply_photo(photo="https://te.legra.ph/file/45ecbe8b5430f2f845ece.jpg", caption="**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ...**")
    response = "**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await app.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await app.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in app.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ 🍡**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
    
    await msg.edit_text(response)
                
