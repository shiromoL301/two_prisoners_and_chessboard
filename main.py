import logging

from src.TwoPrisonersAndChessboard import TwoPrisonersAndChessboard
from config import LANGUAGE, LEVEL, TITLE_TYPE, THEME, LOG_FILE_PATH, LOG_FORMAT

def main():
    logging.basicConfig(filename=LOG_FILE_PATH, filemode='w', level=logging.DEBUG, format=LOG_FORMAT)

    two_prisoners_and_chessboard = TwoPrisonersAndChessboard(
            level=LEVEL,
            gui_theme=THEME,
            language=LANGUAGE,
            players_name=TITLE_TYPE
        )
    two_prisoners_and_chessboard.main_loop()


if __name__ == '__main__':
    main()