import PySimpleGUI as sg

from functools import cached_property
import random
from typing import Any, Generator

from .Cell import Cell, Blank, Pawn
from .GuideText import GuideText
from .patterns import Key, Lang, Player, PlayersName
from .parity_check import parity_check
from .theme import FontTheme, GuiTheme, ColorTheme
from .utils import int2nary, nary2int, xor


class TwoPrisonersAndChessboard:
    def __init__(
            self,
            level: int,
            gui_theme: GuiTheme = GuiTheme(ColorTheme.reddit(), FontTheme.arial()),
            language: Lang=Lang.JA,
            players_name: PlayersName=PlayersName.JAIL_PRISON
        ):
        if level < 1:
            raise ValueError("The Level of the game must be at least 1!!")
        self.text   : GuideText = GuideText(language, players_name)
        self.__level: int       = level
        self.__gui_theme: GuiTheme = gui_theme
        
        self.board: list[list[Cell]] = [[Blank() for _ in range(self.ncols)] for _ in range(self.nrows)]
        self.phase: Player = Player.JAILER
        
        self.flipped: tuple[int, int] = (-1, -1)
        self.secret : int = -1
        self.answer : int = -1
        self.winner : str = ""

        layout: list[list[sg.Element]] = self.build_main_layout()
        self.window = sg.Window(
                self.text.game_title,
                layout,
                size=(self.window_width, self.window_height),
                background_color=self.gui_theme.color_theme.background_color
            )

    @property
    def base_height(self) -> int:
        """ウィンドウの縦幅のベース値．Read Only."""
        return 75
    
    @property
    def base_width(self) -> int:
        """ウィンドウの横幅のベース値．Read Only."""
        return 425
    
    @property
    def minimum_height(self) -> int:
        """ウィンドウの縦幅の最小値．Read Only."""
        return 425
    
    @property
    def square_size(self) -> int:
        """盤面のマスのサイズ．Read Only."""
        return 65
    
    @property
    def window_height(self) -> int:
        """ウィンドウの立幅．Read Only."""
        return max(self.minimum_height, self.square_size * self.ncols + self.base_height)
    
    @property
    def window_width(self) -> int:
        """ウィンドウの横幅．Read Only."""
        return self.square_size * self.nrows + self.base_width
    
    @property
    def level(self) -> int:
        """ゲームの難易度を取得する．Read Only．"""
        return self.__level
    
    @property
    def gui_theme(self) -> GuiTheme:
        """GUIテーマを取得する．Read Only."""
        return self.__gui_theme
    
    @cached_property
    def ncells(self) -> int:
        """盤面のマス数を取得する．Read Only．

        Returns:
            int: 盤面のマス数
        """
        return self.nrows * self.ncols
    
    @cached_property
    def ncols(self) -> int:
        """盤面の列数を取得する．Read Only．

        Returns:
            int: 盤面の列数
        """
        return max(2, self.nrows)
    
    @cached_property
    def nrows(self) -> int:
        """盤面の行数を取得する．Read Only．

        Returns:
            int: 盤面の行数
        """
        return 2 ** (self.level - 1)

    def board_as_ints(self) -> list[list[int]]:
        """盤面を整数の二重リストへ変換する

        Returns:
            list[list[int]]: 盤面の整数二重リスト表現
        """
        return list(map(lambda row: [*map(int, row)], self.board))

    def build_main_layout(self) -> list[list[sg.Element]]:
        """メインレイアウトのビルド

        Returns:
            list[list[sg.Element]]: メインレイアウト
        """
        return [
            [
                sg.Text(
                    self.text.game_title,
                    font=(self.gui_theme.font_theme.title_font, 18),
                    text_color=self.gui_theme.color_theme.title_color,
                    background_color=self.gui_theme.color_theme.background_color
                )
            ],
            [sg.Column(self.generate_board_layout()), sg.Column(self.menu_layout(), background_color=self.gui_theme.color_theme.background_color)]
        ]
    
    def build_random_board(self) -> None:
        """ランダムな盤面のビルド"""
        self.board = self.generate_random_board()
        self.render_board()

    def activate_board(self) -> None:
        """盤面を有効化する"""
        self.enable_elements(*[int2nary(i, self.ncols, length=2) for i in range(self.ncells)])
    
    def deactivate_board(self) -> None:
        """盤面を無効化する"""
        self.disable_elements(*[int2nary(i, self.ncols, length=2) for i in range(self.ncells)])
    
    def disable_elements(self, *keys: tuple[Key]) -> None:
        """要素を無効化する
        
        Args:
            keys: tuple[Key]: 無効化する要素のキー
        """
        for key in keys:
            self.window[key].update(disabled=True) 
    
    def enable_elements(self, *keys: tuple[Key]) -> None:
        """要素を有効化する
        
        Args:
            keys: tuple[Key]: 有効化する要素のキー
        """
        for key in keys:
            self.window[key].update(disabled=False) 
    
    def flip_cell_at(self, location: tuple[int, int]) -> None:
        """マスの反転

        Args:
            location: tuple[int, int]: 盤面の座標
        """
        i, j = location
        self.board[i][j] = Pawn() if isinstance(self.board[i][j], Blank) else Blank()
        self.window[location].update(image_filename=self.board[i][j].get_image_path())
    
    def generate_board_layout(self) -> list[list[sg.PySimpleGUI.ReadButton]]:
        """盤面レイアウトの生成

        Returns:
            list[list[sg.PySimpleGUI.ReadButton]]: 盤面のレイアウト
        """
        return [
            [
                cell.rendered_at(
                    (i, j),
                    light_color=self.gui_theme.color_theme.square_light_color,
                    dark_color=self.gui_theme.color_theme.square_dark_color
                )
                for j, cell in enumerate(row)
            ]
            for i, row in enumerate(self.board)
        ]
    
    def generate_cells_keys(self) -> Generator[tuple[int, int], None, None]:
        """マスを制御するキーの生成

        Yields:
            Generator[tuple[int, int], None, None]: マスを制御するキーのジェネレータ
        """
        for cell_idx in range(self.ncells):
            yield int2nary(cell_idx, self.ncols, length=2)
    
    def generate_random_board(self) -> list[list[Cell]]:
        """ランダムなチェス盤の生成

        Returns:
            list[list[Cell]]: ランダムに生成したチェス盤
        """
        return [[random.choice([Blank(), Pawn()]) for _ in range(self.ncols)] for _ in range(self.nrows)]
    
    def hide_elements(self, *keys: tuple[Key]) -> None:
        """要素を非表示にする

        Args:
            keys: tuple[Key]: 非表示にする要素のキー
        """
        for key in keys:
            self.window[key].update(visible=False)
    
    def is_valid_secret(self) -> bool:
        """秘密値の正当性を検証する

        Returns:
            bool: 秘密値が正当であるか
        """
        return isinstance(self.secret, int) and (1 <= self.secret <= self.ncells)
    
    def log_phase_jailer(self) -> None:
        """看守の操作のログを取る"""
        print(self.text.board_from_jailer)
        print(*(self.board_as_ints()), sep='\n')
        print(self.text.number_from_jailer, self.secret)

    def log_phase_prisoner1(self) -> None:
        """囚人1の操作のログを取る"""
        print(self.text.flipped_cell(self.flipped))
        print(self.text.board_after_flipped)
        print(*(self.board_as_ints()), sep='\n')
    
    def log_phase_prisoner2(self) -> None:
        """囚人2の操作のログを取る"""
        print(self.text.number_from_prisoner2, self.answer)
        print(self.text.result(self.winner))
            
    def render_board(self) -> None:
        """盤面を描画する"""
        for (i, j) in self.generate_cells_keys():
            self.window[(i, j)].update(image_filename=self.board[i][j].get_image_path())
    
    def render_text(
            self,
            text: str,
            key: Any=None,
            visible: bool=True,
            is_accent: bool=False
        ) -> sg.Text:
        """テキストのレンダリング
        
        Args:
            text: str: テキスト

        Returns:
            sg.Text: テキスト要素
        """
        font = self.gui_theme.font_theme.accent_font if is_accent else self.gui_theme.font_theme.text_font
        text_color = self.gui_theme.color_theme.title_color if is_accent else self.gui_theme.color_theme.text_color

        font_size = 12 if is_accent else 10
        return sg.Text(
            text,
            font=(font, font_size),
            text_color=text_color,
            background_color=self.gui_theme.color_theme.background_color,
            key=key,
            visible=visible
        )
     
    def run_confirmation_for_prisoner1(self, location: tuple[int, int]) -> None:
        """囚人1の操作の確認を実行する

        Args:
            location (tuple[int, int]): クリックされたセルの位置
        """
        row = location[0] + 1
        col = location[1] + 1
        sub_layout = [
            [sg.Text(
                self.text.confirm_removal_pawn_at(location) if self.board[row-1][col-1]
                else self.text.confirm_placement_pawn_at(location)
            )],
            [sg.Button(self.text.yes, key=Key.YES), sg.Button(self.text.no, key=Key.NO)]
        ]
        sub_window = sg.Window(self.text.confirmation_screen, sub_layout, size=(300, 100))
        
        self.deactivate_board()

        while True:
            sub_event, _ = sub_window.read()
            
            match sub_event:
                case Key.YES:
                    self.flip_cell_at(location)
                    self.flipped = location
                    self.window[Key.SUBMIT].update(text=self.text.next, visible=True)
                    self.hide_elements(Key.WARNING)
                    self.log_phase_prisoner1()
                    break
                case Key.NO | sg.WIN_CLOSED:
                    self.activate_board()
                    break
        
        sub_window.close()        

    def run_jailer_phase(self, jailer_player: str) -> None:
        """看守のターンを実行する

        Args:
            jailer_player: str: 看守のプレイヤー．self.text.player または self.text.cpu．
        """
        self.disable_elements(Player.JAILER, Player.PRISONER1, Player.PRISONER2, Key.START)                
        self.activate_board() 
        self.window[Key.PHASE].update(value=self.text.phase(self.phase))
        self.window[Key.INSTRUCTION].update(value=self.text.jailer_instruction(self.ncells))
        
        match jailer_player:
            case self.text.player:
                self.show_elements(Key.SECRET, Key.SUBMIT)
                
            case self.text.cpu:
                self.window[Key.PHASE].update(value=self.text.phase(self.phase))
                self.window[Key.SECRET].update(value=random.randint(1, self.ncells))
                self.build_random_board()
                self.deactivate_board()
                self.window[Key.INSTRUCTION].update(value=self.text.jailer_log)
                self.window[Key.SUBMIT].update(text=self.text.next, visible=True)
    
    def run_prisoner1_phase(self, prisoner1_player: str) -> None:
        """囚人1のターンを実行する

        Args:
            prisoner1_player: str: 囚人1のプレイヤー．self.text.player または self.text.cpu．
        """
        self.log_phase_jailer()
        self.hide_elements(Key.SECRET, Key.SUBMIT, Key.WARNING)
        self.phase = Player.PRISONER1
        self.window[Key.PHASE].update(value=self.text.phase(self.phase))
        
        if prisoner1_player == self.text.player:
            self.activate_board()
            self.window[Key.INSTRUCTION].update(value=self.text.prisoner1_instruction)
            self.window[Key.WARNING].update(value=self.text.display_jailer_secret(self.secret), visible=True)
        else:
            secret_binary = int2nary(self.secret, 2, length=self.ncols)
            parity = parity_check(self.board)
            parities = int2nary(parity, 2, length=self.ncols)
            flipping_binary = xor(secret_binary, parities)
            flipping_label = nary2int(flipping_binary, 2)
            self.flipped = int2nary(flipping_label, self.ncols, length=2) 
            self.flip_cell_at(self.flipped)
            
            print(self.text.secret_binary, secret_binary)
            print(self.text.board_parities, parities)
            print(self.text.result_of_xor, flipping_binary)
            self.log_phase_prisoner1()
            self.window[Key.INSTRUCTION].update(value=self.text.prisoner1_log)
            self.window[Key.SUBMIT].update(text=self.text.next, visible=True)
    
    def run_prisoner2_phase(self, prisoner2_player: str) -> None:
        """囚人2のターンを実行する

        Args:
            prisoner2_player: str: 囚人2のプレイヤー．self.text.player または self.text.cpu．
        """
        self.phase = Player.PRISONER2
        self.window[Key.PHASE].update(value=self.text.phase(self.phase))
        self.hide_elements(Key.SUBMIT, Key.WARNING)
        if prisoner2_player == self.text.player:
            self.window[Key.INSTRUCTION].update(value=self.text.prisoner2_instruction)
            self.window[Key.SECRET].update(value=1, visible=True)
            self.window[Key.SUBMIT].update(text=self.text.ok, visible=True)
        else:
            self.answer = parity_check(self.board)
            self.window[Key.INSTRUCTION].update(value=self.text.answer_by_prisoner2(self.answer))
            self.window[Key.SUBMIT].update(text=self.text.confirm_result, visible=True)
    
    def run_winner_judgement(self, values: dict[Any, Any]) -> None:
        """勝者判定を実行する

        Args:
            values (dict[Any, Any]): Windowオブジェクトから生成される値
        """
        if values[Player.PRISONER2] == self.text.player:
            self.answer = values[Key.SECRET]
        self.disable_elements(Key.SECRET, Key.SUBMIT)
        self.show_elements(Key.FINISH)
        
        if self.answer == self.secret:
            self.winner = self.text.prisoner
            winner_text = self.text.prisoners_victory
        else:
            self.winner = self.text.jailer
            winner_text = self.text.jailer_victory 
        self.window[Key.WARNING].update(value=winner_text, visible=True)
        self.log_phase_prisoner2()

    def show_elements(self, *keys: tuple[Key]) -> None:
        """要素を表示する

        Args:
            keys: tuple[Key]: 表示する要素のキー
        """
        for key in keys:
            self.window[key].update(visible=True)
            
    def menu_layout(self) -> list[list[sg.Element]]:
        """メニューレイアウトの取得

        Returns:
            list[list[sg.Element]]: メニューレイアウト
        """
        return [
            [self.render_text(self.text.player_settings, is_accent=True)],
            [
                self.render_text(f'{self.text.jailer}:'),
                sg.Combo(
                    [self.text.player, self.text.cpu],
                    default_value=self.text.player,
                    key=Player.JAILER,
                    readonly=True
                )
            ],
            [
                self.render_text(f'{self.text.prisoner}1:'),
                sg.Combo(
                    [self.text.player, self.text.cpu],
                    default_value=self.text.player,
                    key=Player.PRISONER1,
                    readonly=True
                )
            ],
            [
                self.render_text(f'{self.text.prisoner}2:'),
                sg.Combo(
                    [self.text.player, self.text.cpu],
                    default_value=self.text.player,
                    key=Player.PRISONER2,
                    readonly=True
                )
            ],
            [sg.Button(self.text.start, key=Key.START)],
            [self.render_text('', key=Key.PHASE, is_accent=True)],
            [self.render_text('', key=Key.INSTRUCTION)],
            [
                sg.Combo(
                    list(range(1, self.ncells+1)),
                    default_value=1,
                    visible=False,
                    key=Key.SECRET
                ),
                sg.Button(self.text.ok, key=Key.SUBMIT, visible=False)
            ],
            [sg.Text(
                '',
                font=(self.gui_theme.font_theme.accent_font, 12),
                background_color=self.gui_theme.color_theme.background_color,
                key=Key.WARNING,
                text_color=self.gui_theme.color_theme.accent_color,
                visible=False
            )],
            [sg.Button(self.text.finish, visible=False, key=Key.FINISH)]
        ] 

    def main_loop(self):
        """ゲームの開始"""
        while True:
            event, values = self.window.read()

            if event in self.generate_cells_keys():
                match self.phase:
                    case Player.JAILER:
                        self.flip_cell_at(event)     
                    case Player.PRISONER1: 
                        self.run_confirmation_for_prisoner1(event)
                    case _:
                        pass
                  
            match event:
                case Key.START:
                    self.run_jailer_phase(values[Player.JAILER]) 
                
                case Key.SUBMIT: 
                    match self.phase:
                        case Player.JAILER:
                            self.secret = values[Key.SECRET]
                            if self.is_valid_secret():
                                self.run_prisoner1_phase(values[Player.PRISONER1])
                            else:
                                self.window[Key.WARNING].update(visible=True, value=self.text.validation(self.ncells))
                        case Player.PRISONER1:
                            self.run_prisoner2_phase(values[Player.PRISONER2])
                        case Player.PRISONER2:
                            self.run_winner_judgement(values) 
                        case _:
                            pass
                
                case Key.FINISH | sg.WIN_CLOSED:
                    break

                case _:
                    pass
        
        self.window.close()