from enum import Enum

class Key(Enum):
    FINISH      = '-FINISH-'
    INSTRUCTION = '-INSTRUCTION-'
    NO          = '-NO-'
    PHASE       = '-PHASE-'
    SECRET      = '-SECRET-'
    START       = '-START-'
    SUBMIT      = '-SUBMIT-'
    WARNING     = '-WARNING-'
    YES         = '-YES-'


class Lang(Enum):
    EN = "English"
    JA = "Japanese"        


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