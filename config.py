from src.theme import ColorTheme, FontTheme, GuiTheme
from src.patterns import PlayersName, Lang

LEVEL = 4  # 1以上(6以下推奨)
TITLE_TYPE = PlayersName.JAIL_PRISON
LANGUAGE = Lang.JA
COLOR_THEME = ColorTheme.reddit()
FONT_THEME = FontTheme.natural()
THEME = GuiTheme(COLOR_THEME, FONT_THEME)

IMAGE_ROOT = 'images/'
LOG_ROOT = 'log/'

LOG_FORMAT = '[%(levelname)s] %(funcName)s at line %(lineno)d | %(asctime)s\n%(message)s'
LOG_FILENAME = 'two_prisoners_and_chessboard.log'
