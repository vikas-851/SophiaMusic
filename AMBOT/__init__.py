from AMBOT.core.bot import Anony
from AMBOT.core.dir import dirr
from AMBOT.core.git import git
from AMBOT.core.userbot import Userbot
from AMBOT.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
