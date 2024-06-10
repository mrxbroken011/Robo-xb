import asyncio
import os
import requests
from platform import python_version as pyver
from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver
from JarvisRobo import SUPPORT_CHAT, pbot, BOT_USERNAME, OWNER_ID, BOT_NAME, START_IMG

# Video URL
VIDEO_URL = "https://telegra.ph/file/a80214e1fa190281c6c73.mp4"

# Inline keyboard markup
Jarvis = [
    [
        InlineKeyboardButton(text="ᴊᴀʀᴠɪs", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/broknxsupport"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

@pbot.on_message(filters.command("alive"))
async def send_alive_message(client, message: Message):
    # Download the video file
    video_file_path = "video.mp4"
    response = requests.get(VIDEO_URL)
    with open(video_file_path, "wb") as file:
        file.write(response.content)

    # Send the video
    await message.delete()
    accha = await message.reply("📲")
    await asyncio.sleep(0.2)
    await accha.edit("ʙʀᴏᴋᴇɴ ɪs ᴄᴀᴄʜɪɴɢ ᴅᴀᴛᴀ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴄᴏʀᴇ ᴀɴᴀʟʏsᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...")
    await asyncio.sleep(0.1)
    await accha.edit("😈ᴛɪɢᴇʀ ᴢɪɴᴅᴀ ʜᴀɪ..")
    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await message.reply_sticker("CAACAgEAAx0Cfbdm0QACATVmC-2FuLpqFS0KfIHldXuM8eTtjwACsQQAAsW0uURrdxdu_gmoNh4E")
    await umm.delete()
    await asyncio.sleep(0.2)
    await message.reply_video(
        video=video_file_path,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
━━━━━━━━━━━━━━━━━━━
» **ᴍʏ ᴏᴡɴᴇʀ :** [ᴏᴡɴᴇʀ](https://t.me/aboutbrokenx)

» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`

» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`

» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`

» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(Jarvis),
    )

    # Delete the downloaded video file
    os.remove(video_file_path)
