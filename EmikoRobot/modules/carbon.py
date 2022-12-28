from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from EmikoRobot import pbot
from EmikoRobot.utils.errors import capture_err
from EmikoRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/e081c4a428c2d4593bd73.jpg"


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **Hey I'm Victor** 

**Owner of repo : [Flame](https://t.me/ricks_2005)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`
** My collaborators**
** 1) [𝐅𝐥𝐚𝐦𝐞 ✗ℋ𝐚𝐬𝐡𝐢𝐫𝐚 『ARCANE』 • ᴢᴇxᴛ™](https://t.me/ricks_2005)**

**Sorry but the repo is not available.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Network", url="https://t.me/Hashira_Association"
                    ),
                    InlineKeyboardButton(
                        "Support", url="https://t.me/Victor_Nikiforov_Support"
                    ),
                ]
            ]
        ),
    )
