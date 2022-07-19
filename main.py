import logging
import os

from src.TwoPrisonersAndChessboard import TwoPrisonersAndChessboard
from config import LANGUAGE, LEVEL, TITLE_TYPE, THEME, LOG_FILENAME, LOG_FORMAT, LOG_PATH


def main():
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    log_file_path = f'{LOG_PATH}/{LOG_FILENAME}'
    logging.basicConfig(filename=log_file_path, filemode='w',
                        level=logging.DEBUG, format=LOG_FORMAT)

    two_prisoners_and_chessboard = TwoPrisonersAndChessboard(
        level=LEVEL,
        gui_theme=THEME,
        language=LANGUAGE,
        players_name=TITLE_TYPE
    )
    two_prisoners_and_chessboard.main_loop()


if __name__ == '__main__':
    main()
