from pyrogram import Client, filters
from pyrogram.types import Message
from Imshivaexe import startTime
from Imshivaexe import get_uptime
import time 
from config import HANDLER as hl
from Imshivaexe import grt
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("ping",  hl) & filters.me)
async def ping(client, message):
    r = await client.get_me()
    st = time.time()
    end = time.time()
    user = r.mention
    upt = get_uptime(time.time())
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    PING = f"""
__ᏕᎷᎧᏦᏋᏒ 𝘼𝘿𝘿𝙞𝙘𝙩𝙞𝙤𝙣ᜰ꙰ꦿ🍷__

__**๏ 𝗣𝗶𝗻𝗴 𝗢𝗳 𝗦𝗺𝗼𝗸𝗲𝗿 𝗕𝗼𝘁 ⚡ »**__ `{pong}`
__**๏ 𝗨𝗽𝘁𝗶𝗺𝗲 𝗢𝗳 𝗦𝗺𝗼𝗸𝗲𝗿 𝗕𝗼𝘁 ⚡ »**__ `{upt}`
**__๏ 𝗨𝘀𝗲𝗿 𝗢𝗳 𝗦𝗺𝗼𝗸𝗲𝗿 𝗕𝗼𝘁 ⚡ »__** {user}
"""
    return await message.edit(PING)
