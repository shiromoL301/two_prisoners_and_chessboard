from .patterns import Lang, Player, PlayersName

class GuideText:
    def __init__(self, lang: Lang=Lang.JA, players_name: PlayersName=PlayersName.JAIL_PRISON):
        self.lang = lang
        self.players_name = players_name
    
    def answer_by_prisoner2(self, answer: int) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.prisoner}2の回答は「{answer}」です。"
            case _:
                return f"The answer submitted by {self.prisoner}2\nis ``{answer}''"

    @property
    def board_after_flipped(self) -> str:
        match self.lang:
            case Lang.JA:
                return "変更後のチェス盤の状態:"
            case _:
                return "Board after flipped:"
    
    @property
    def board_from_jailer(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.jailer}が渡したチェス盤:"
            case _:
                return f"Chessboard received from {self.jailer}"
    
    @property
    def board_parities(self) -> str:
        match self.lang:
            case Lang.JA:
                return "盤面のパリティ:"
            case _:
                return "Parities of the chessboard:"
    
    @property
    def confirmation_screen(self) -> str:
        match self.lang:
            case Lang.JA:
                return "確認画面"
            case _:
                return "Confirmation"
    
    def confirm_placement_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.JA:
                return f"{row}行{col}列目にポーンを設置しますか？"
            case _:
                return f"Do you want to place pawn \nin row {row}, column {col}?"
    
    def confirm_removal_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.JA:
                return f"{row}行{col}列目のポーンを取り除きますか？"
            case _:
                return f"Do you want to remove pawn \nin row {row}, column {col}?"
    
    @property
    def confirm_result(self) -> str:
        match self.lang:
            case Lang.JA:
                return "結果を見る"
            case _:
                return "See the result"
    
    @property
    def cpu(self) -> str:
        match self.lang:
            case _:
                return "CPU"
    
    def display_jailer_secret(self, secret: int) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.jailer}が選んだ数字は「{secret}」です。"
            case _:
                return f"The {self.jailer}'s chosen number is ``{secret}''."
    
    @property
    def finish(self) -> str:
        match self.lang:
            case Lang.JA:
                return "終了"
            case _:
                return "Finish"
    
    def flipped_cell(self, location: tuple[int, int]) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.JA:
                return f"{self.prisoner}1が変更したマス: {row}行{col}列目"
            case _:
                return f"Flipped Square by {self.prisoner}1: {row}-th row, {col}-th column"
    
    @property
    def game_title(self) -> str:
        match self.lang:
            case Lang.JA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "2人の幼女とチェス盤の部屋"
                    case PlayersName.DLR_CHL:
                        return "2人の挑戦者とチェス盤問題"
                    case _:
                        return "2人の囚人とチェス盤問題"
            case _:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Room with Two Little Girls and a Chessboard"
                    case PlayersName.DLR_CHL:
                        return "Chessboard Problem with Two Challengers"
                    case _:
                        return "Two Prisoners and a Chessboard"
    
    @property
    def jailer(self) -> str:
        match self.lang:
            case Lang.JA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "悪魔"
                    case PlayersName.DLR_CHL:
                        return "ディーラー"
                    case _:
                        return "看守"
            case _:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Devil"
                    case PlayersName.DLR_CHL:
                        return "Dealer"
                    case _:
                        return "Jailer"

    def jailer_instruction(self, max_num:int) -> str:
        match self.lang:
            case Lang.JA:
                return f'{self.jailer}はポーンを配置し、1～{max_num}のうち、\n好きな数字を選択してください。'
            case _:
                return f'The person playing the role of the {self.jailer} should\nplace the pawn and choose any number\nfrom 1 to {max_num}'
    
    @property
    def jailer_log(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.jailer}がポーンの配置と数字を決定しました。"
            case _:
                return f"The {self.jailer} determined the placement of pawns\nand a secret number."
    
    @property
    def jailer_victory(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"不正解です！{self.jailer}の勝利！！"
            case _:
                return f"Mission failure! The {self.jailer} wins!"
    
    @property
    def next(self) -> str:
        match self.lang:
            case Lang.JA:
                return "次へ"
            case _:
                return "Next"
    
    @property
    def no(self) -> str:
        match self.lang:
            case Lang.JA:
                return "いいえ"
            case _:
                return "No"
    
    @property
    def number_from_jailer(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.jailer}が選択した数字:"
            case _:
                return f"Number chosen by {self.jailer}:"
    
    @property
    def number_from_prisoner2(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.prisoner}2が選択した数字:"
            case _:
                return f"Number chosen by {self.prisoner}2"
    
    @property
    def ok(self) -> str:
        match self.lang:
            case Lang.JA:
                return "決定"
            case _:
                return "OK"
    
    def phase(self, player: Player) -> str:
        match player:
            case Player.JAILER:
                pname = self.jailer
            case Player.PRISONER1:
                pname = f"{self.prisoner}1"
            case Player.PRISONER2:
                pname = f"{self.prisoner}2"
        match self.lang:
            case Lang.JA:
                return f"【{pname}のターン】"
            case _:
                return f"[{pname} Phase]"
    
    @property
    def player(self) -> str:
        match self.lang:
            case _:
                return "Player"
    
    @property
    def player_settings(self) -> str:
        match self.lang:
            case Lang.JA:
                return "【プレイヤー設定】"
            case _:
                return "[Player Settings]"

    @property
    def prisoner(self) -> str:
        match self.lang:
            case Lang.JA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "幼女"
                    case PlayersName.DLR_CHL:
                        return "挑戦者"
                    case _:
                        return "囚人"
            case _:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Girl"
                    case PlayersName.DLR_CHL:
                        return "Challenger"
                    case _:
                        return "Prisoner"
    
    @property
    def prisoner1_instruction(self) -> str:
        match self.lang:
            case Lang.JA:
                return f'{self.prisoner}1は看守の番号が{self.prisoner}2に伝わるように\nチェス盤のマスを1つ選択してください。\nポーンがあれば排除し、ポーンがなければ\n設置します。'
            case _:
                return f"The person playing the role of {self.prisoner} 1 should\nchange one square on the chessboard so that\nthe {self.prisoner} 2 can reveal the {self.jailer}'s chosen\nnumber."
    @property
    def prisoner1_log(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.prisoner}1がチェス盤の状態を1箇所変更しました。"
            case _:
                return f"{self.prisoner}1 changed one of the squares\nin the chessboard."
    
    @property
    def prisoner2_instruction(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.prisoner}2はチェス盤の状態から\n{self.jailer}の数字を当ててください。"
            case _:
                return f"The person playing the role of the {self.prisoner}2\nshould guess the number set by the {self.jailer}\nfrom the state of the chessboard."
    
    @property
    def prisoners_victory(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"正解です！{self.prisoner}の勝利！！"
            case _:
                return f"Congratulations! {self.prisoner}s win!"
    
    def result(self, winner: str) -> str:
        match self.lang:
            case Lang.JA:
                return f"結果: {winner}の勝利"
            case _:
                return f"Winner: {winner}"
    
    @property
    def result_of_xor(self) -> str:
        match self.lang:
            case Lang.JA:
                return "排他的論理和の結果:"
            case _:
                return "The results of exclusive or:"
    
    @property
    def secret_binary(self) -> str:
        match self.lang:
            case Lang.JA:
                return f"{self.jailer}の数字の2進数表現:"
            case _:
                return f"Binary representation of {self.jailer}'s chosen number:"
    
    @property
    def start(self) -> str:
        match self.lang:
            case Lang.JA:
                return "スタート"
            case _:
                return "Start" 
    
    def validation(self, max_num: int) -> str:
        match self.lang:
            case Lang.JA:
                return f"1以上{max_num}以下の整数を入力してください！"
            case _:
                return f"Input value must be an integer between 1 and {max_num}!"
    
    @property
    def yes(self) -> str:
        match self.lang:
            case Lang.JA:
                return "はい"
            case _:
                return "Yes"