import PySimpleGUI as sg

import datetime
import os
import shutil
from typing import Any

from config import DEFAULT_LEVEL, LOG_ROOT, LOG_FILE_SUFFIX, DEFAULT_TITLE_TYPE
from src.TwoPrisonersAndChessboard import TwoPrisonersAndChessboard

from .guide_text import GuideText
from .patterns import Key, Lang, Player, PlayerType, PlayersName, Text
from .theme import ColorTheme, FontTheme, GuiTheme

class App:
    def __init__(self, language: Lang=Lang.ENG, players_name: PlayersName=PlayersName.JAIL_PRISON):
        self.language = language
        self.players_name = players_name
        self.game_count = 0
        self.last_game_id = 0

        layout = [
            [sg.Text(self.text().game_title, font=(None, 18), key=Text.TITLE)],
            [self.player_settings_module(), self.extra_settings_module()],
            [
                sg.Button(self.text().start, key=Key.START),
                sg.Text("", key=Key.LAST_GAME_ID, visible=False),
                sg.Button(self.text().clear_logs, key=Key.CLEAR, visible=False)
            ],
        ]
        
        self.window = sg.Window(
            self.text().game_title,
            layout,
            size=(580, 250),
            resizable=True
        )
    
    def text(self) -> GuideText:
        return GuideText(self.language, self.players_name)
    
    def language_dict(self, str2enum=False) -> dict[Lang, str]:
        return {
            "中文"    : Lang.CHS,
            "English" : Lang.ENG,
            "Français": Lang.FRA,
            "Italiano": Lang.ITA,
            "日本語"  : Lang.JPN,
        } if str2enum else {
            Lang.CHS: "中文",
            Lang.ENG: "English",
            Lang.FRA: "Français",
            Lang.ITA: "Italiano",
            Lang.JPN: "日本語",
        }    

    def extra_settings_module(self) -> sg.Column:
        """各種設定用モジュールの取得

        Returns:
            sg.Column: 各種設定用モジュール
        """
        return sg.Column([
            [sg.Text(self.text().ui_settings, font=(None, 12), key=Text.UI_SETTINGS)],
            [
                sg.Text(self.text().language, key=Text.LANGUAGE),
                sg.Combo(
                    [*self.language_dict().values()],
                    default_value=self.language_dict()[self.language],
                    key=Key.LANGUAGE,
                    readonly=True,
                    enable_events=True
                )
            ],
            [
                sg.Text(self.text().color_theme, key=Text.COLOR_THEME),
                sg.Combo(
                    list(ColorTheme.get_catalog(str2enum=True).keys()),
                    default_value="Reddit",
                    key=Key.COLOR_THEME,
                    readonly=True
                )
            ],
            [
                sg.Text(self.text().font_theme, key=Text.FONT_THEME),
                sg.Combo(
                    list(FontTheme.get_catalog(str2enum=True).keys()),
                    default_value="Natural",
                    key=Key.FONT_THEME,
                    readonly=True
                )
            ]
        ], key=Key.PLAYER_SETTINGS)
    
    def player_settings_module(self) -> sg.Column:
        """プレイヤー設定モジュールの取得

        Returns:
            sg.Column: プレイヤー設定モジュール
        """
        return sg.Column([
            [sg.Text(self.text().player_settings, font=(None, 12), key=Text.PLAYER_SETTINGS)],
            [
                sg.Text(self.text().level, key=Text.LEVEL),
                sg.Combo(
                    list(range(1, 8)),
                    default_value=DEFAULT_LEVEL,
                    key=Key.LEVEL,
                    readonly=True
                )
            ],
            [
                sg.Text(f'{self.text().jailer}:', key=Text.JAILER),
                sg.Combo(
                    [self.text().player, self.text().cpu],
                    default_value=self.text().player,
                    key=Player.JAILER,
                    readonly=True
                )
            ],
            [
                sg.Text(f'{self.text().prisoner}1:', key=Text.PRISONER1),
                sg.Combo(
                    [self.text().player, self.text().cpu],
                    default_value=self.text().player,
                    key=Player.PRISONER1,
                    readonly=True
                )
            ],
            [
                sg.Text(f'{self.text().prisoner}2:', key=Text.PRISONER2),
                sg.Combo(
                    [self.text().player, self.text().cpu],
                    default_value=self.text().player,
                    key=Player.PRISONER2,
                    readonly=True
                )
            ]
        ], key=Key.PLAYER_SETTINGS)
    
    def rerender_window(self):
        self.window[Text.TITLE].update(value=self.text().game_title)
        self.window[Text.PLAYER_SETTINGS].update(value=self.text().player_settings)
        self.window[Text.LEVEL].update(value=self.text().level)
        self.window[Text.JAILER].update(value=f"{self.text().jailer}:")
        self.window[Text.PRISONER1].update(value=f"{self.text().prisoner}1:")
        self.window[Text.PRISONER2].update(value=f"{self.text().prisoner}2:")
        self.window[Text.UI_SETTINGS].update(value=self.text().ui_settings)
        self.window[Text.LANGUAGE].update(value=self.text().language)
        self.window[Text.COLOR_THEME].update(value=self.text().color_theme)
        self.window[Text.FONT_THEME].update(value=self.text().font_theme)
        self.window[Key.START].update(text=self.text().start)
        self.window[Key.LAST_GAME_ID].update(value=f"{self.text().last_game_id}: {self.last_game_id}")
        self.window[Key.CLEAR].update(text=self.text().clear_logs)
    
    def create_log_file(self, values: dict[str, str]) -> tuple[str, int]:
        if not os.path.exists(LOG_ROOT):
            os.makedirs(LOG_ROOT)
        
        dt_now = datetime.datetime.now()
        self.last_game_id = abs(hash(dt_now.strftime('%Y/%m/%d %H:%M:%S')))
        self.window[Key.LAST_GAME_ID].update(value=f"{self.text().last_game_id}: {self.last_game_id}", visible=True)
        self.window[Key.CLEAR].update(visible=True)
        log_file_path = f"{LOG_ROOT}/{LOG_FILE_SUFFIX}{self.last_game_id}.log"
        buffer = [
            f"{dt_now.strftime(f'[START] {self.text().nth_play(self.game_count)} | Game ID: {self.last_game_id} | %H-%M-%S %Y/%m/%d')}\n",
            f"{self.text().player_settings}\n",
            f"{self.text().jailer}: {values[Player.JAILER]}\n",
            f"{self.text().prisoner}1: {values[Player.PRISONER1]}\n",
            f"{self.text().prisoner}2: {values[Player.PRISONER2]}\n"
        ]
        with open(log_file_path, 'w') as f:
            f.writelines(buffer)
        
        return log_file_path
    
    def clear_logs(self):
        shutil.rmtree(LOG_ROOT)
        os.mkdir(LOG_ROOT)
    
    def create_new_game(self, values):
        self.game_count += 1
        level = int(values[Key.LEVEL])
        color_theme = ColorTheme.get_catalog(str2enum=True)[values[Key.COLOR_THEME]]
        font_theme = FontTheme.get_catalog(str2enum=True)[values[Key.FONT_THEME]]
        gui_theme = GuiTheme(color_theme, font_theme)
        language =  [key for key, value in self.language_dict().items() if value == values[Key.LANGUAGE]][0]
        
        log_file_path = self.create_log_file(values)
        jailer_type    = PlayerType.Player if values[Player.JAILER]    == self.text().player else PlayerType.CPU
        prisoner1_type = PlayerType.Player if values[Player.PRISONER1] == self.text().player else PlayerType.CPU
        prisoner2_type = PlayerType.Player if values[Player.PRISONER2] == self.text().player else PlayerType.CPU

        two_prisoners_and_chessboard = TwoPrisonersAndChessboard(
            level=level,
            jailer_type=jailer_type,
            prisoner1_type=prisoner1_type,
            prisoner2_type=prisoner2_type,
            gui_theme=gui_theme,
            language=language,
            players_name=DEFAULT_TITLE_TYPE,
            log_file_path=log_file_path,
            game_id=self.last_game_id
        )
        two_prisoners_and_chessboard.main_loop()

    def main_loop(self):
        """メインの処理"""        
        while True:
            event, values = self.window.read()
            match event:
                case Key.START:
                    self.create_new_game(values)
                
                case Key.LANGUAGE:
                    self.language = self.language_dict(str2enum=True)[values[Key.LANGUAGE]]
                    self.rerender_window()
                
                case Key.CLEAR:
                    self.clear_logs()
                    
                case sg.WIN_CLOSED:
                    break
                case _:
                    pass
        
        self.window.close()