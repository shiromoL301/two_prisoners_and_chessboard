from src.theme import ColorTheme, FontTheme, GuiTheme
from src.patterns import PlayersName, Lang

LEVEL = 4  # 1以上
TITLE_TYPE = PlayersName.JAIL_PRISON
LANGUAGE = Lang.JA
COLOR_THEME = ColorTheme.reddit()
FONT_THEME = FontTheme.natural()
THEME = GuiTheme(COLOR_THEME, FONT_THEME)

IMAGE_PATH = 'images/'
LOG_PATH = 'log/'

LOG_FORMAT = '[%(levelname)s] %(funcName)s at line %(lineno)d | %(asctime)s\n%(message)s'
LOG_FILENAME = 'two_prisoners_and_chessboard.log'
