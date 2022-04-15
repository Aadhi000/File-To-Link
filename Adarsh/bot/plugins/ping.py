# Telegram Ping / Pong Speed

from pyrogram import filters
from Adarsh.bot import StreamBot
import time

@StreamBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    jv = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await jv.edit(f"Pong!\n{time_taken_s:.3f} ms")
