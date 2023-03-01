import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "20171745"))
API_HASH = os.environ.get("API_HASH", "0c02173d06c7f4916e0181e2c989a363")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5600148348:AAFscHiLLFsGmnE1VOOXTa9Jfoh3UH6bVCA")
DROPLINK_API = os.environ.get("DROPLINK_API","37ca781d294530c4198510ed8ac0d6fef8109ccb")
MDISK_API = os.environ.get("MDISK_API", "neRblmUPT2bDq65y6iDb")
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertorBotpro")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Sohanrazz:Sohanrazz@cluster0.3ru2c4f.mongodb.net/?retryWrites=true&w=majority")
WEBSITE = os.environ.get('WEBSITE', "Oggylink.com")

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split("-1001859917060")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "True")), True)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/SohanRazz/bulk-channel-link")
USERNAME = os.environ.get("USERNAME", "Netflix_Hindi_Movies_4K2")
HEADER_TEXT = os.environ.get("HEADER_TEXT", ',')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", ',')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "True")), True)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False
