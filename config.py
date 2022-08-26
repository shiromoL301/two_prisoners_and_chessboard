from src.theme import ColorTheme, FontTheme, GuiTheme
from src.patterns import PlayersName, Lang

DEFAULT_LEVEL = 4  # 1以上(6以下推奨)
DEFAULT_TITLE_TYPE = PlayersName.JAIL_PRISON
DEFAULT_LANGUAGE = Lang.JPN
DEFAULT_COLOR_THEME = ColorTheme.reddit()
DEFAULT_FONT_THEME = FontTheme.natural()
DEFAULT_THEME = GuiTheme(DEFAULT_COLOR_THEME, DEFAULT_FONT_THEME)

IMAGE_ROOT = 'images/'
LOG_ROOT = 'log/'

LOG_FORMAT = '[%(levelname)s] %(funcName)s at line %(lineno)d | %(asctime)s\n%(message)s'
LOG_FILE_SUFFIX = 'game'
