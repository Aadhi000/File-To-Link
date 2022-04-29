# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start","help","login🔑","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start","help","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('start')) & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/fe4a250011485ef19e763.jpg",
                caption="<i>ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ɴᴏᴡ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="HTML",
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/fe4a250011485ef19e763.jpg",
        caption =f'**𝙷𝙴𝙻𝙻𝙾...⚡**\n\n**𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃.**\n\n**𝙸 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴𝚂 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙾𝙽𝙻𝙸𝙽𝙴 & 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶..\n\n𝚄𝚂𝙴 /help 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙳𝙴𝚃𝙰𝙸𝙻𝚂...\n\n𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴 𝚃𝙾 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉....**',
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 ⚡", url="https://t.me/MWUpdatez"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/OpusTechz")],
                    [InlineKeyboardButton("💸 𝙳𝙾𝙽𝙰𝚃𝙴 💸", url="https://paypal.me/114912Aadil"), InlineKeyboardButton("💠 𝙶𝙸𝚃𝙷𝚄𝙱 💠", url="https://github.com/Aadhi000")],
                    [InlineKeyboardButton("💌 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 💌", url="https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")]
                ]
            ),
            disable_web_page_preview=True


@StreamBot.on_message((filters.command("help") | filters.regex('help')) & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/fe4a250011485ef19e763.jpg",
                Caption="**𝙹𝙾𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚃𝙾 𝚄𝚂𝙴 ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**┣⪼ 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝙴𝙽 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝚂𝙷𝙰𝚁𝙰𝙱𝙻𝙴 𝙻𝙸𝙽𝙺 𝙾𝙵 𝙸𝚃...\n\n┣⪼ 𝚃𝙷𝙸𝚂 𝙻𝙸𝙽𝙺 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙾𝚁 𝚃𝙾 𝚂𝚃𝚁𝙴𝙰𝙼 𝚄𝚂𝙸𝙽𝙶 𝙴𝚇𝚃𝙴𝚁𝙽𝙰𝙻 𝚅𝙸𝙳𝙴𝙾 𝙿𝙻𝙰𝚈𝙴𝚁𝚂 𝚃𝙷𝚁𝙾𝚄𝙶𝙷 𝙼𝚈 𝚂𝙴𝚁𝚅𝙴𝚁.\n\n┣⪼ 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶 𝙹𝚄𝚂𝚃 𝙲𝙾𝙿𝚈 𝚃𝙷𝙴 𝙻𝙸𝙽𝙺 𝙰𝙽𝙳 𝙿𝙰𝚂𝚃𝙴 𝙸𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾 𝙿𝙻𝙰𝚈𝙴𝚁 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶.\n\n┣⪼ 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝚂𝙾 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂. 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽 𝚃𝙾 𝙶𝙴𝚃 𝚁𝙴𝙰𝙻𝚃𝙸𝙼𝙴 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙴𝚅𝙴𝚁𝚈 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝙿𝙾𝚂𝚃../\n\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴**""",
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 ⚡", url="https://t.me/MWUpdatez"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/OpusTechz")],
                [InlineKeyboardButton("💸 𝙳𝙾𝙽𝙰𝚃𝙴 💸", url="https://paypal.me/114912Aadil"), InlineKeyboardButton("💠 𝙶𝙸𝚃𝙷𝚄𝙱 💠", url="https://github.com/Aadhi000")],
                [InlineKeyboardButton("💌 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 💌", url="https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")]
            ]
        )
    )
