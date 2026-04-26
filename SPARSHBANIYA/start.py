from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ButtonStyle

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/d3pmlk.jpg",
        caption=f"""━━━━━━━━━━━━━━━━━━━━
    ★ **{me2}** ★
━━━━━━━━━━━━━━━━━━━━

✦ **нєу** {msg.from_user.mention} **!**

▸ ɪ'ᴍ ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ
▸ ꜱᴜᴘᴘᴏʀᴛꜱ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ
▸ ꜰᴀꜱᴛ & ꜱᴇᴄᴜʀᴇ

━━━━━━━━━━━━━━━━━━━━
**ᴜꜱᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ**
━━━━━━━━━━━━━━━━━━━━

✨ **ᴏᴡɴᴇʀ:** [⏤͟͞ 𝙎𝙋𝘼𝙍𝙎𝙃 𝘽𝘼𝙉𝙄𝙔𝘼](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✨ ɢᴇɴᴇʀᴀᴛᴇ ɴᴏᴡ ✨", callback_data="generate", style=ButtonStyle.PRIMARY)
                ],
                [
                    InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/BANIYA_BOTS", style=ButtonStyle.SUCCESS),
                    InlineKeyboardButton("📡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/BANIYA_UPDATES", style=ButtonStyle.SUCCESS)
                ],
                [
                    InlineKeyboardButton("🔗 sᴏᴜʀᴄᴇ", url="https://github.com/TeamBaniya/BANIYA_STRING", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data="help", style=ButtonStyle.PRIMARY)
                ]                
            ]
        )
    )


# Help button callback handler
@Client.on_callback_query(filters.regex("help"))
async def help_callback(bot: Client, callback_query):
    await callback_query.answer()
    
    help_text = """━━━━━━━━━━━━━━━━━━━━
    ★ **ʜᴏᴡ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ** ★
━━━━━━━━━━━━━━━━━━━━

✦ **ꜱᴛᴇᴘ 1:** 
   ᴄʟɪᴄᴋ ᴏɴ 「✨ ɢᴇɴᴇʀᴀᴛᴇ ɴᴏᴡ ✨」 ʙᴜᴛᴛᴏɴ

✦ **ꜱᴛᴇᴘ 2:**
   ᴄʜᴏᴏꜱᴇ ʏᴏᴜʀ ᴘʀᴇꜰᴇʀʀᴇᴅ ʟɪʙʀᴀʀʏ:
   • ᴘʏʀᴏɢʀᴀᴍ / ᴘʏʀᴏɢʀᴀᴍ ᴠ2
   • ᴛᴇʟᴇᴛʜᴏɴ
   • ʙᴏᴛ ᴛᴏᴋᴇɴ (ᴘʏʀᴏɢʀᴀᴍ/ᴛᴇʟᴇᴛʜᴏɴ)

✦ **ꜱᴛᴇᴘ 3:**
   ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴀᴘɪ_ɪᴅ** ᴀɴᴅ **ᴀᴘɪ_ʜᴀꜱʜ**
   (ᴛʏᴘᴇ /ꜱᴋɪᴘ ᴛᴏ ᴜꜱᴇ ʙᴏᴛ'ꜱ ᴀᴘɪ)

✦ **ꜱᴛᴇᴘ 4:**
   ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ** (ᴡɪᴛʜ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ)
   ᴇxᴀᴍᴘʟᴇ: `+91 9876543210`

✦ **ꜱᴛᴇᴘ 5:**
   ᴇɴᴛᴇʀ ᴛʜᴇ **ᴏᴛᴘ** ʏᴏᴜ ʀᴇᴄᴇɪᴠᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ
   (ꜱᴇɴᴅ ɪᴛ ᴡɪᴛʜ ꜱᴘᴀᴄᴇꜱ: `1 2 3 4 5`)

✦ **ꜱᴛᴇᴘ 6:**
   ɪꜰ 2-ꜱᴛᴇᴘ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ, ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ

✦ **ꜱᴛᴇᴘ 7:**
   ʏᴏᴜʀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ **ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ**

━━━━━━━━━━━━━━━━━━━━
**⚠️ ᴡᴀʀɴɪɴɢ:**
• ᴅᴏ ɴᴏᴛ ꜱʜᴀʀᴇ ʏᴏᴜʀ ꜱᴛʀɪɴɢ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ
• ᴋᴇᴇᴘ ɪᴛ ꜱᴇᴄʀᴇᴛ ꜰᴏʀ ꜱᴇᴄᴜʀɪᴛʏ
━━━━━━━━━━━━━━━━━━━━

✨ **ᴏᴡɴᴇʀ:** [⏤͟͞ 𝙎𝙋𝘼𝙍𝙎𝙃 𝘽𝘼𝙉𝙄𝙔𝘼](tg://user?id={OWNER_ID})"""

    await callback_query.message.edit_caption(
        caption=help_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("◀️ ʙᴀᴄᴋ", callback_data="back_to_start", style=ButtonStyle.PRIMARY)
                ]
            ]
        )
    )


# Back button callback handler
@Client.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(bot: Client, callback_query):
    await callback_query.answer()
    me2 = (await bot.get_me()).mention
    
    await callback_query.message.edit_caption(
        caption=f"""━━━━━━━━━━━━━━━━━━━━
    ★ **{me2}** ★
━━━━━━━━━━━━━━━━━━━━

✦ **нєу** {callback_query.from_user.mention} **!**

▸ ɪ'ᴍ ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ
▸ ꜱᴜᴘᴘᴏʀᴛꜱ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ
▸ ꜰᴀꜱᴛ & ꜱᴇᴄᴜʀᴇ

━━━━━━━━━━━━━━━━━━━━
**ᴜꜱᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ**
━━━━━━━━━━━━━━━━━━━━

✨ **ᴏᴡɴᴇʀ:** [⏤͟͞ 𝙎𝙋𝘼𝙍𝙎𝙃 𝘽𝘼𝙉𝙄𝙔𝘼](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✨ ɢᴇɴᴇʀᴀᴛᴇ ɴᴏᴡ ✨", callback_data="generate", style=ButtonStyle.PRIMARY)
                ],
                [
                    InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/GIRLSSOCIETYLINK", style=ButtonStyle.SUCCESS),
                    InlineKeyboardButton("📡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Requirements_json", style=ButtonStyle.SUCCESS)
                ],
                [
                    InlineKeyboardButton("🔗 sᴏᴜʀᴄᴇ", url="https://github.com/TeamBaniya/BANIYA_STRING", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data="help", style=ButtonStyle.PRIMARY)
                ]                
            ]
        )
    )
