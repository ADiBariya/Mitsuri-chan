import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Mitsuri.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from Mitsuri import app

MISHI = [
    "https://te.legra.ph/file/f9565a7c3951eca7b4831.jpg",
    "https://te.legra.ph/file/b34ebf3a2b894fb0a48d7.jpg",
    "https://te.legra.ph/file/f4184cc626904dbdffe43.jpg",
    "https://te.legra.ph/file/f1077eba265ca7dc31b03.jpg",
    "https://te.legra.ph/file/62261a6a5083ac6ece19a.jpg",
    "https://te.legra.ph/file/68051cb812bb44ee3a543.jpg",
    "https://te.legra.ph/file/981e6cfd3663195d170f1.jpg",
    "https://te.legra.ph/file/5b1409234c333a282a4cf.jpg"
    "https://te.legra.ph/file/921be7c78df9568152e23.jpg",
    "https://te.legra.ph/file/068aecd628b3e559146dc.jpg",
    "https://te.legra.ph/file/78f6a01f83fdbf5e97d17.jpg",
    "https://te.legra.ph/file/5735f848623c562968bab.jpg",
    "https://te.legra.ph/file/482bd428b26eebde18160.jpg",
    "https://te.legra.ph/file/f40dbdb22b575ae928a22.jpg",
    "https://te.legra.ph/file/829e3d05a8b65785fa644.jpg",
    "https://te.legra.ph/file/62261a6a5083ac6ece19a.jpg",
    "https://te.legra.ph/file/d1471af58227db49731fb.jpg",
    "https://te.legra.ph/file/0fc3165657c1bc41983d0.jpg",
]


ROY = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/Mitsuri_Robot?startgroup=true"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/Ahjin_sprt")
    ],
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**♥︎ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ♥︎**

**๏ ɴᴀᴍᴇ** ➛ {message.from_user.mention}
**๏ ᴜsᴇʀ ɪᴅ** ➛ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**♥︎ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**♥︎ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**♥︎ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg, reply_markup=InlineKeyboardMarkup(ROY),)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")

    
