from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from pyrogram.types import Message
import asyncio


@Bunny.on_message(filters.command(["kiss", "kissi"], hl) & filters.me)
async def hearts(client: Client, message: Message):
    await message.edit("🤵‍♂               👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂            👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂       👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂💋👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂💋👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂💋👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂💋👰‍♀")
