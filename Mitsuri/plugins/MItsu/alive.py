import time

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import filters
from Mitsuri import app as sung, StartTime
from Mitsuri.utils.formatters import get_readable_time

final_txt = """
Hᴇʏ, ɪᴛᴢ Mɪᴛsᴜʀɪ
━━━━━━━••⌜ᴀʟɪᴠᴇ⌟••━━━━━━━
➤ Oᴡɴᴇʀ : [Oʙᴀɴᴀɪ Sᴀɴ](https://t.me/Hotoke_fr)
• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : 2.0.106
• ᴜᴘᴛɪᴍᴇ : {uptime}
━━━━━━━━•••••••••━━━━━━━━
[sᴜᴘᴘᴏʀᴛ](https://t.me/Ahjin_sprt) | [ᴜᴘᴅᴀᴛᴇs](https://t.me/Mitsuri_Updates)
"""

alive_vid = "https://telegra.ph/file/a8ad8e669231f392fa245.mp4"


@sung.on_message(filters.command("alive"))
async def alive_cmd(client, message: Message):
    await message.reply_video(
        alive_vid,
        caption=final_txt.format(uptime=get_readable_time((time.time() - StartTime))),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Add Me To Your Group",
                        url="https://telegram.dog/Mitsuri_Robot?startgroup=true",
                    )
                ]
            ]
        ),
    )