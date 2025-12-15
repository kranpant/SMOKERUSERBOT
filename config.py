import os
from os import getenv

""" Here is all variables we need for deploy userbot"""

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "20790743")) # API_ID get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "266b46661c0eb26ee0cb9ef7dfebfe39") # API_HASH get it from my.telegram.org

# SESSIONS ~ Telegram 
SESSION = os.getenv("SESSION", "BQDqPPEAod-HE4M4m-IBaqFG6fiedu2a5btrr__LbLw8OWwC-hfCWWhDcIAw5t3k8UkRJVmtwtTF3kIt0HHOohmAPiUFcEt_OoZJWEWm16Ike3MrU3GXAQc1RhsCZ6CQyC5bwPGzWO9AWRYXOaXNmbu8jZhL3rhFz4fA-BoaMH597uA6Hd4iICA0XBjDwqQxsydiXwptVFwq11-BtSI8zF-3i3bjUdu-D5gFD6PXwD7LD00fevP1ELG0J4K51SnKqdlweyW1U3oV6PVuXuAqolJAHNqXJ4lquk0a7OEPGcwzmoFKJUJlcm5hsAVC9XI0L9XBHr58Pbr44lxcjOqZ8ClRooAbGwAAAAHm6hnSAA") # SESSION get it by @RaBBiTSessionBot on Telegram 
TOKEN = os.getenv("TOKEN", "6750645277:AAEIUykLlU1Bt-4snxYCkIcggfeQJiKeyxk") # BOT_TOKEN get it by @BotFather on Telegram 
LOGGER_ID = int(getenv("LOGGER_ID", "-1002075664729")) # LOGGER_ID fill here your logs telegram group id

# HANDLER ~ Telegram 
HANDLER = os.getenv("HANDLER", ".") # HANDLER fill here your command trigger

# DATABASES ~ mongodb.com
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://kranpant_db_user:kranpant_db_user@cluster0.xy6tc02.mongodb.net/?appName=Cluster0") # MONGO_URI fill here mongodb database url get it by mongodb.com

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
