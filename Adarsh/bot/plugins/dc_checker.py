from Adarsh.bot import StreamBot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """ Your Telegram DC Is : `{}`  """

@StreamBot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )
