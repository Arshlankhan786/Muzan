import re
import os
from os import environ
from Script import script

# Regex pattern for IDs
id_pattern = re.compile(r'^-?\d+$')

# Helper functions
def is_enabled(value, default=True):
    if isinstance(value, str):
        if value.lower() in ["true", "yes", "1", "enable", "y"]:
            return True
        elif value.lower() in ["false", "no", "0", "disable", "n"]:
            return False
    return default

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                 r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                 r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                 r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# -------------------------------
# Main Bot Variables
# -------------------------------
API_ID = int(environ.get('API_ID', '20588632'))
API_HASH = environ.get('API_HASH', '86381c7fcfd83ca9bb16f920b6f132b3')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.match(admin) else admin for admin in environ.get('ADMINS', '5554060579 5683891175').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/flipkartlootzs")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001915187457'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/pathans_movies')

# -------------------------------
# Images
# -------------------------------
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/GBd.jpg')
START_IMG = environ.get('START_IMG', '').split() or [
    'https://graph.org/file/af54c50978d7bd219d38a.jpg',
    'https://graph.org/file/e41349ea48fd7e5324ac3.jpg',
    'https://graph.org/file/1dff8a8429b6a52a0e0cc.jpg',
    'https://graph.org/file/7bfdd6ab09c1423ee0bdd.jpg',
    'https://graph.org/file/02ec1b10f3bc9fbef2a1d.jpg'
]
FSUB_PICS = environ.get('FSUB_PICS', '').split() or ['https://graph.org/file/7478ff3eac37f4329c3d8.jpg']

# -------------------------------
# File Limit
# -------------------------------
IS_FILE_LIMIT = is_enabled(environ.get('IS_FILE_LIMIT', 'True'))
FILES_LIMIT = int(environ.get("FREE_FILES", "2"))

# -------------------------------
# Database Settings
# -------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Pathan:pathan@cluster0.b0zqbsl.mongodb.net/?retryWrites=true&w=majority")
FILES_DATABASE_URL = environ.get('FILES_DATABASE_URL', DATABASE_URI)
SECOND_FILES_DATABASE_URL = environ.get('SECOND_FILES_DATABASE_URL', DATABASE_URI)
DATABASE_NAME = environ.get('DATABASE_NAME', "Auto-filter-muzan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# -------------------------------
# Verify / Shortlink Settings
# -------------------------------
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', LOG_CHANNEL))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', LOG_CHANNEL))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

# Shortener defaults
SHORTENER_API = environ.get("SHORTENER_API", "default_api")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'gplinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", '')
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", '')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# -------------------------------
# Force Subscribe Settings
# -------------------------------
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "")
auth_channels = environ.get("AUTH_CHANNELS", "")
# Only include numeric IDs
AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)]
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]

# -------------------------------
# Channels
# -------------------------------
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001972484628'))
request_channel = environ.get('REQUEST_CHANNEL', '')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.match(request_channel) else None

# -------------------------------
# Movie / Auto Index
# -------------------------------
MOVIE_UPDATE_NOTIFICATION = is_enabled(environ.get('MOVIE_UPDATE_NOTIFICATION', 'True'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002984412963'))
CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('CHANNELS', '-1001672766292').split()]
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002984412963'))
IMAGE_FETCH = is_enabled(environ.get('IMAGE_FETCH', 'True'))
LINK_PREVIEW = is_enabled(environ.get('LINK_PREVIEW', 'False'))
ABOVE_PREVIEW = is_enabled(environ.get('ABOVE_PREVIEW', 'True'))
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
TMDB_POSTER = is_enabled(environ.get('TMDB_POSTER', 'False'))
LANDSCAPE_POSTER = is_enabled(environ.get('LANDSCAPE_POSTER', 'True'))

# -------------------------------
# Bot Settings
# -------------------------------
AUTO_FILTER = is_enabled(environ.get('AUTO_FILTER', 'True'))
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', 'True'))
DELETE_TIME = int(environ.get('DELETE_TIME', '3000'))
IMDB = is_enabled(environ.get('IMDB', 'False'))
FILE_CAPTION = environ.get('FILE_CAPTION', getattr(script, 'FILE_CAPTION', ''))
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', getattr(script, 'IMDB_TEMPLATE_TXT', ''))
LONG_IMDB_DESCRIPTION = is_enabled(environ.get('LONG_IMDB_DESCRIPTION', 'True'))
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', 'False'))
SPELL_CHECK = is_enabled(environ.get('SPELL_CHECK', 'True'))
LINK_MODE = is_enabled(environ.get('LINK_MODE', 'True'))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'False'))

# -------------------------------
# Filters
# -------------------------------
LANGUAGES = [("ʜɪɴᴅɪ", "hin"), ("ᴇɴɢʟɪsʜ", "eng"), ("ᴛᴇʟᴜɢᴜ", "telugu"), ("ᴛᴀᴍɪʟ", "tamil"),
             ("ᴋᴀɴɴᴀᴅᴀ", "kannada"), ("ᴍᴀʟᴀʏᴀʟᴀᴍ", "malayalam"), ("ʙᴇɴɢᴀʟɪ", "ben"),
             ("ᴍᴀʀᴀᴛʜɪ", "marathi"), ("ɢᴜᴊᴀʀᴀᴛɪ", "gujarati"), ("ᴘᴜɴᴊᴀʙɪ", "punjabi")]
QUALITIES = [ "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p"]
SEASONS = [("sᴇᴀsᴏɴ 𝟷", "s01"), ("sᴇᴀsᴏɴ 𝟸", "s02"), ("sᴇᴀsᴏɴ 𝟹", "s03"), ("sᴇᴀsᴏɴ 𝟺", "s04"),
           ("sᴇᴀsᴏɴ 𝟻", "s05"), ("sᴇᴀsᴏɴ 𝟼", "s06"), ("sᴇᴀsᴏɴ 𝟽", "s07"), ("sᴇᴀsᴏɴ 𝟿", "s09"),
           ("sᴇᴀsᴏɴ 𝟷𝟶", "s10")]

# -------------------------------
# Stream Settings
# -------------------------------
IS_PREMIUM_STREAM = is_enabled(environ.get('IS_PREMIUM_STREAM', 'True'))
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1002984412963"))
URL = environ.get("URL", "https://feminist-marketa-muzanbot-ee3c813c.koyeb.app/")
if not URL.endswith("/"):
    URL += "/"
# -------------------------------
# Settings array for captions & shortener
# -------------------------------
settings = {
    'caption': FILE_CAPTION or 'Default caption here',
    'api': SHORTENER_API or 'default_api',
    'shortner': SHORTENER_WEBSITE or 'gplinks.com',
    'api2': SHORTENER_API2 or '',
    'shortner2': SHORTENER_WEBSITE2 or '',
    'api3': SHORTENER_API3 or '',
    'shortner3': SHORTENER_WEBSITE3 or ''
}
