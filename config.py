#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6324741766:AAF0e__jV5swZs2SayylLUxPC-a_CuZUrP0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24091153"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1b5ef3db9cc5a04ea168c4982a956fdf")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002251341853"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7276947730"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://honnjurczaktaxs3073:21rx3afEYmb7rCtM@cluster0.dbvkh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster01")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002236411344"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002163908097"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002189543598"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#token varibles
# my shortner https://dashboard.shareus.io/signup/lifetime/U9AZbV

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "6848b60ae73cfa371e404a949dd315051728df81")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","gojfsi/2")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n 𝐌𝐞 𝐡𝐮 𝐟𝐢𝐥𝐞 𝐬𝐭𝐨𝐫𝐞 𝐛𝐨𝐭 , 𝐦𝐞 𝐭𝐮𝐦𝐤𝐨 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 𝐟𝐢𝐥𝐞𝐬 𝐝𝐞𝐭𝐚 𝐡𝐮 𝐏𝐞𝐡𝐥𝐞 𝐚𝐤 𝐚𝐝 𝐝𝐞𝐤𝐡𝐨 𝐨𝐫 𝐤𝐮𝐜𝐡 𝐉𝐚𝐧𝐧𝐚 𝐡𝐚𝐢 𝐭𝐨 :- » @Mrxofficalx</b>")
try:
    ADMINS=[7014219411]
    for x in (os.environ.get("ADMINS", "1114789110").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝙋𝙚𝙝𝙡𝙚 𝙣𝙞𝙘𝙝𝙚 𝙠𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙟𝙤𝙞𝙣 𝙆𝙖𝙧𝙤 𝘽𝙝𝙖𝙞 𝙡𝙤𝙜...!\n\n 𝙎𝙞𝙢𝙥𝙡𝙚 𝙨𝙖 1 𝙖𝙙 𝙙𝙚𝙠𝙝𝙤 24 𝙝𝙤𝙪𝙧𝙨 𝙠𝙚 𝙡𝙞𝙮𝙚 𝙗𝙤𝙩 𝙪𝙨𝙚 𝙠𝙖𝙧𝙤..!\n\n 𝙎𝙖𝙢𝙟𝙝 𝙣𝙞 𝙖 𝙧𝙖 𝙝𝙖𝙞 𝙩𝙤 [ 𝙃𝙤𝙬 𝙩𝙤 𝙪𝙨𝙚 𝙩𝙝𝙚 𝙗𝙤𝙩 ] 𝙢𝙚 𝙘𝙡𝙞𝙘𝙠 𝙆𝙖𝙧𝙤..!\n\n 𝐀𝐠𝐚𝐫 𝐤𝐨𝐢 𝐩𝐫𝐨𝐛𝐥𝐞𝐦 𝐚 𝐑𝐚𝐡𝐢 𝐡𝐚𝐢 𝐭𝐨 𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐦𝐞 𝐛𝐚𝐭𝐚𝐨 :- @xman_help ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @AF_mhakal</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @AF_Mhakal"

ADMINS.append(OWNER_ID)
ADMINS.append(7014219411)

LOG_FILE_NAME = "codeflixbots.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
