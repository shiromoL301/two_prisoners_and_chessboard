from enum import Enum

class Key(Enum):
    ALL             = '-ALL-'
    CLEAR           = '-CLEAR-'
    FINISH          = '-FINISH-'
    INSTRUCTION     = '-INSTRUCTION-'
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
    CHI = "Chinese"
    EN  = "English"
    FR  = "French"
    JA  = "Japanese"        


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
