import os
from os import getenv

""" Here is all variables we need for deploy userbot"""

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "20790743")) # API_ID get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "266b46661c0eb26ee0cb9ef7dfebfe39") # API_HASH get it from my.telegram.org

# SESSIONS ~ Telegram 
SESSION = os.getenv("SESSION", "BQGhGGQAOisDT3y_cFQsR8B44Y79BMx9RQCqkbqKMrau0DPNv5hhsIk8Tu2PZ2Odn5UtZEb9bzwPhhWcQ3HVY2EmSZa9HD8aGNA1rqMIBStLQEc1yyFWBWCTsSXwvWO9ObNgxFmpzASoZ2KLzturl28aHGalp6RYPqgyJzHSvoirOL30oZ61N2nBRZPlrye1sHXuJjeeCYj5s-GLYEIZmcJ6-p0atOMKsElPh266a4heMTOwpYSHtlp_T9Cv_XbRvikaQ6hP7wIp3pfgzEPnGYRau5iatQgytISBRpXomNU2XL99ku6VGELUilfxPHuQKpZZ1_LOBr8zyh9FZ-cn9xVUjOdJAgAAAAFucWqFAA") # SESSION get it by @RaBBiTSessionBot on Telegram 
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
