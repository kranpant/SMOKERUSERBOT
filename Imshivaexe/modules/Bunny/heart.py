from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from pyrogram.types import Message
import asyncio

@Bunny.on_message(filters.command(["heart", "love"], hl) & filters.me)
async def hearts(client: Client, message: Message):
    await message.edit("❤️")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await message.edit("❤️ I Love You <3")
