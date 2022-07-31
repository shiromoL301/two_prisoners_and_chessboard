from enum import Enum

class Key(Enum):
    ALL             = '-ALL-'
    CLEAR           = '-CLEAR-'
    COLOR_THEME     = '-COLOR_THEME-'
    FINISH          = '-FINISH-'
    FONT_THEME      = '-FONT_THEME-'
    INSTRUCTION     = '-INSTRUCTION-'
    LANGUAGE        = '-LANGUAGE-'
    LAST_GAME_ID    = '-LAST_GAME_ID-'
    LEVEL           = '-LEVEL-'
    NO              = '-NO-'
    PHASE           = '-PHASE-'
    PLAYER_SETTINGS = '-PLAYER_SETTINGS-'
    RANDOM          = '-RANDOM-'
    SECRET          = '-SECRET-'
    START           = '-START-'
    SUBMIT          = '-SUBMIT-'
    WARNING         = '-WARNING-'
    YES             = '-YES-'


class Lang(Enum):
    CHS = "Chinese"
    ENG = "English"
    FRA = "French"
    ITA = "Italy"
    JPN = "Japanese"        


class Player(Enum):
    JAILER    = "Jailer"
    PRISONER1 = "Prisoner1"
    PRISONER2 = "Prisoner2"


class PlayersName(Enum):
    DEVIL_GIRL  = "Devil and Girls" 
    DLR_CHL     = "Dealer and Challengers"
    JAIL_PRISON = "Jailer and Prisoner"


class PlayerType(Enum):
    CPU    = "CPU"
    Player = "Player"

class Text(Enum):
    TITLE = "-TITLE-"
    PLAYER_SETTINGS = "-PLAYER_SETTINGS-"
    LEVEL = "-LEVEL-"
    JAILER = "-JAILER-"
    PRISONER1 = "-PRISONER1-"
    PRISONER2 = "-PRISONER2-"
    UI_SETTINGS = "-UI_SETTINGS-"
    LANGUAGE = "-LANGUAGE-"
    COLOR_THEME = "-COLOR_THEME-"
    FONT_THEME = "-FONT_THEME-"