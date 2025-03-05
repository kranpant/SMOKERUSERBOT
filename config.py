import os
from os import getenv

""" Here is all variables we need for deploy userbot"""

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "20790743")) # API_ID get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "266b46661c0eb26ee0cb9ef7dfebfe39") # API_HASH get it from my.telegram.org

# SESSIONS ~ Telegram 
SESSION = os.getenv("SESSION", "BQEvjOkAIxoKy4M0qwUDsjARdm_b7CQci2qvgwyClGzWxTbny2StzCWv-UbM6cjh6G3DzoLgkSvrACx6fOuiVscCpWWDfwJyaCmLHQabyXCMHIArqJR2NUb41AZnqiwQudTcc6jI00IwsJ9yk2E3Jz3VJvKi8Bw9AGPVuEInwpL3NUgOuF5c32vrcHgJrHaDPL5K5AivOzAHEAxILF6KX9qDcqINEOua8qSyz99D20L3dVFI6fbRFxu0F0t9k8YIJOByNidAyauobuQPY2T2qMoem3F8P8eWZ3m84N94cvesQftn2auP6q0NRMvYw8iU2YEqlkYsvA9UMFtvK0QQgBZv6HnldwAAAAHMx7MCAA") # SESSION get it by @RaBBiTSessionBot on Telegram 
TOKEN = os.getenv("TOKEN", "6405960633:AAFNeckpR29AtqLRppGpqIZq_4frZHdIHmk") # BOT_TOKEN get it by @BotFather on Telegram 
LOGGER_ID = int(getenv("LOGGER_ID", "-1002379258977")) # LOGGER_ID fill here your logs telegram group id

# HANDLER ~ Telegram 
HANDLER = os.getenv("HANDLER", ".") # HANDLER fill here your command trigger

# DATABASES ~ mongodb.com
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://kranpantmain:ueaWKwac1qJsKCpq@cluster0.pqump.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # MONGO_URI fill here mongodb database url get it by mongodb.com

# PORN ~ spam
ALLOW_PORN = getenv("ALLOW_PORN", True) # u can enable and disable porn spam from here 

""" © @Imshivaexe """
#-----------------------------------------------------------------------------------------
""" You don't need to edit beyond this. """

ALIVE_PIC = os.getenv("ALIVE_PIC", "")
if not ALIVE_PIC:
    ALIVE_PIC = "https://telegra.ph/file/dfe3bf37f969e4464393b.jpg"
    
HELP_PIC = os.getenv("HELP_PIC", "")
if not HELP_PIC:
    HELP_PIC = "https://telegra.ph/file/dfe3bf37f969e4464393b.jpg"

PM_PIC = os.getenv("PM_PIC", "")
if not PM_PIC:
    PM_PIC = "https://telegra.ph/file/dfe3bf37f969e4464393b.jpg"

NEWS_API = os.getenv("NEWS_API", "")
if not NEWS_API:
    NEWS_API = "140dd16908d54879b350d0c7378306a5"

WEATHER_API = os.getenv("WEATHER_API", "")
if not WEATHER_API:
    WEATHER_API = "fadd97c7821d568d82f1cceaa06c7def"
    
BLACKLIST_CHAT = [
    -1002084534383,
]

BIO = getenv("BIO", "")
if not BIO:
    BIO = "⚡𝗦𝗺𝗼𝗸𝗲𝗿 𝗔𝗱𝗱𝗶𝗰𝘁𝗶𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗨𝘀𝗲𝗿⚡"
