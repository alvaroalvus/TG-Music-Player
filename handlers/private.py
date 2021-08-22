from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""hei✨️ iam Olivia🎸 𝐈𝐚𝐦 𝐀𝐧 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐆𝐫𝐨𝐮𝐩𝐬 𝐌𝐮𝐬𝐢𝐜 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭🎶✨.

The commands I currently support are:

/play - 🎶 Type the name of the song or YouTube video 
/pause - ▶️ Pause the audio stream 
/resume - ⏸ Resume the audio stream 
/skip - ↪️ Skip the current audio stream
/mute - 🔇 Mute the userbot
/unmute - 🔊 Unmute the userbot
/stop - 🗑🛑 Clear the queue and remove the userbot from the call
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/Team_Satanz_Fed"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Olivia_VC_Support"
                    )
                ]
            ]
        )
    )
