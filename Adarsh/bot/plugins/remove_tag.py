# (c) Jigarvarma2005
from pyrogram.errors import RPCError
from pyrogram import filters
from Adarsh.bot import StreamBot
from Adarsh.bot.plugins.stream import channel_receive_handler

@StreamBot.on_message(filters.channel & (filters.forwarded | filters.via_bot))
async def forward_channel_handler(client, message):
    try:
        jv_message = await message.copy(message.chat.id)
        await message.delete()
    except RPCError as lel:
        print(lel)
        return
    except:
        return
    await channel_receive_handler(client, jv_message)
