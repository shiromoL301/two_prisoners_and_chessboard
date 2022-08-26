from src.App import App
from config import DEFAULT_LANGUAGE, DEFAULT_TITLE_TYPE


def main():
    app = App(
        language=DEFAULT_LANGUAGE,
        players_name=DEFAULT_TITLE_TYPE
    )
    app.main_loop()


if __name__ == '__main__':
    main()
