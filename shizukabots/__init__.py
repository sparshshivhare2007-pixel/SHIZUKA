from shizukabots.core.bot import Aviax
from shizukabots.core.dir import dirr
from shizukabots.core.git import git
from shizukabots.core.userbot import Userbot
from shizukabots.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
