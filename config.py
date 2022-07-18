from src.theme import ColorTheme, FontTheme, GuiTheme
from src.patterns import PlayersName, Lang

LEVEL = 4 # 1以上
TITLE_TYPE = PlayersName.JAIL_PRISON
LANGUAGE = Lang.JA
COLOR_THEME = ColorTheme.reddit()
FONT_THEME = FontTheme.natural()
THEME = GuiTheme(COLOR_THEME, FONT_THEME)

IMAGE_PATH = 'images/'