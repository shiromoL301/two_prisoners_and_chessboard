from .patterns import Lang, Player, PlayersName

class GuideText:
    def __init__(self, lang: Lang=Lang.JA, players_name: PlayersName=PlayersName.JAIL_PRISON):
        self.lang = lang
        self.players_name = players_name
    
    @property
    def all(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "全部"
            case Lang.FR:
                return "Tous"
            case Lang.JA:
                return "全配置"
            case _:
                return "All"
    
    def answer_by_prisoner2(self, answer: int) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.prisoner}2提交的答案是{answer}。"
            case Lang.FR:
                return f"La réponse soumise par le {self.prisoner} 2\nest ``{answer}''"
            case Lang.JA:
                return f"{self.prisoner}2の回答は「{answer}」です。"
            case _:
                return f"The answer submitted by {self.prisoner} 2\nis ``{answer}''"

    @property
    def board_after_flipped(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "变化后的棋盘状态:"
            case Lang.FR:
                return "Échiquier après avoir été modifié:"
            case Lang.JA:
                return "変更後のチェス盤の状態:"
            case _:
                return "Board after flipped:"
    
    @property
    def board_from_jailer(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"从{self.jailer}那里收到棋盘:"
            case Lang.FR:
                return f"Échiquier reçu de {self.jailer}:"
            case Lang.JA:
                return f"{self.jailer}が渡したチェス盤:"
            case _:
                return f"Chessboard received from {self.jailer}:"
    
    @property
    def board_parities(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "棋盘式奇偶校验位序列:"
            case Lang.FR:
                return "Parités de l'échiquier:"
            case Lang.JA:
                return "盤面のパリティ:"
            case _:
                return "Parities of the chessboard:"
    
    @property
    def clear(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "全部清除"
            case Lang.FR:
                return "Clair"
            case Lang.JA:
                return "クリア"
            case _:
                return "Clear"

    @property
    def confirmation_screen(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "确认屏幕"
            case Lang.FR:
                return "Confirmation"
            case Lang.JA:
                return "確認画面"
            case _:
                return "Confirmation"
    
    def confirm_placement_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHI:
                return f"你想在第{row}行第{col}列设置一个棋子吗？"
            case Lang.FR:
                return f"Voulez-vous placer le pion dans la ligne {row}, colonne {col}?"
            case Lang.JA:
                return f"{row}行{col}列目にポーンを設置しますか？"
            case _:
                return f"Do you want to place pawn \nin row {row}, column {col}?"
    
    def confirm_removal_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHI:
                return f"移除第{row}行和第{col}行的棋子？"
            case Lang.FR:
                return f"Voulez-vous retirer le pion de la ligne {row}, colonne {col}?"
            case Lang.JA:
                return f"{row}行{col}列目のポーンを取り除きますか？"
            case _:
                return f"Do you want to remove pawn \nin row {row}, column {col}?"
    
    @property
    def confirm_result(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "检查结果"
            case Lang.FR:
                return "Confirmez le résultat"
            case Lang.JA:
                return "結果を見る"
            case _:
                return "Confirm the result"
    
    @property
    def cpu(self) -> str:
        match self.lang:
            case _:
                return "CPU"
    
    def display_jailer_secret(self, secret: int) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.jailer}选择的数字是'{secret}'。"
            case Lang.FR:
                return f"Le numéro choisi par le {self.jailer} est le ``{secret}''."
            case Lang.JA:
                return f"{self.jailer}が選んだ数字は「{secret}」です。"
            case _:
                return f"The {self.jailer}'s chosen number is ``{secret}''." 
     
    @property
    def finish(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "结束"
            case Lang.FR:
                return "Finition"
            case Lang.JA:
                return "終了"
            case _:
                return "Finish"
    
    def flipped_cell(self, location: tuple[int, int]) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHI:
                return f"由{self.prisoner}1修改的广场：第{row}行，第{col}列。"
            case Lang.FR:
                return f"Carré retourné par le {self.prisoner} 1 : ligne {row}, colonne {col}."
            case Lang.JA:
                return f"{self.prisoner}1が変更したマス: {row}行{col}列目"
            case _:
                return f"Flipped Square by {self.prisoner} 1: row {row}, column {col}"
    
    @property
    def game_title(self) -> str:
        match self.lang:
            case Lang.CHI:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "有两个年轻女孩和一个棋盘的房间"
                    case PlayersName.DLR_CHL:
                        return "两个挑战者和一个棋盘问题"
                    case _:
                        return "两个囚犯和棋盘问题"
            case Lang.FR:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Chambre avec deux petites filles et un échiquier."
                    case PlayersName.DLR_CHL:
                        return "Problème d'échiquier avec deux challengers."
                    case _:
                        return "Deux prisonniers et un problème d'échiquier"
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
            case Lang.CHI:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "魔鬼"
                    case PlayersName.DLR_CHL:
                        return "经销商"
                    case _:
                        return "狱卒"
            case Lang.FR:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Diable"
                    case PlayersName.DLR_CHL:
                        return "Croupier"
                    case _:
                        return "Geôlier"
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
            case Lang.CHI:
                return f"{self.jailer}放置棋子并选择1至{max_num}之间的任何数字。"
            case Lang.FR:
                return f"La personne jouant le rôle du {self.jailer} doit placer\nle pion et choisir un nombre\nquelconque de 1 à {max_num}."
            case Lang.JA:
                return f'{self.jailer}はポーンを配置し、1～{max_num}のうち、\n好きな数字を選択してください。'
            case _:
                return f'The person playing the role of the {self.jailer} should\nplace the pawn and choose any number\nfrom 1 to {max_num}'
    
    @property
    def jailer_log(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.jailer}决定棋子的位置和数量。"
            case Lang.FR:
                return f"Le {self.jailer} a déterminé le placement des pions\net un nombre secret."
            case Lang.JA:
                return f"{self.jailer}がポーンの配置と数字を決定しました。"
            case _:
                return f"The {self.jailer} determined the placement of pawns\nand a secret number."
    
    @property
    def jailer_victory(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"不正确! {self.jailer}们赢了!"
            case Lang.FR:
                return f"Échec de la mission ! Le {self.jailer} gagne!"
            case Lang.JA:
                return f"不正解です！{self.jailer}の勝利！！"
            case _:
                return f"Mission failure! The {self.jailer} wins!"
    
    @property
    def next(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "下一步"
            case Lang.FR:
                return "Suivant"
            case Lang.JA:
                return "次へ"
            case _:
                return "Next"
    
    @property
    def no(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "不是"
            case Lang.FR:
                return "Non"
            case Lang.JA:
                return "いいえ"
            case _:
                return "No"
    
    @property
    def number_from_jailer(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.jailer}选择的数字:"
            case Lang.FR:
                return f"Numéro choisi par le {self.jailer}:"
            case Lang.JA:
                return f"{self.jailer}が選択した数字:"
            case _:
                return f"Number chosen by {self.jailer}:"
    
    @property
    def number_from_prisoner2(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.prisoner}2选择的数字:"
            case Lang.FR:
                return f"Numéro choisi par le {self.prisoner} 2."
            case Lang.JA:
                return f"{self.prisoner}2が選択した数字:"
            case _:
                return f"Number chosen by {self.prisoner}2"
    
    @property
    def ok(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "决定"
            case Lang.FR:
                return "OK"
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
            case Lang.CHI:
                return f"[{pname}的转变]"
            case Lang.FR:
                return f"Phase de {pname}"
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
            case Lang.CHI:
                return "[播放器设置]"
            case Lang.FR:
                return "[Paramètres du joueur]"
            case Lang.JA:
                return "【プレイヤー設定】"
            case _:
                return "[Player Settings]"

    @property
    def prisoner(self) -> str:
        match self.lang:
            case Lang.CHI:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "小女孩"
                    case PlayersName.DLR_CHL:
                        return "挑战者"
                    case _:
                        return "囚犯"
            case Lang.FR:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Petite Fille"
                    case PlayersName.DLR_CHL:
                        return "Challenger"
                    case _:
                        return "Prisonnier"
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
            case Lang.CHI:
                return f"{self.prisoner}1应该在棋盘上选择一个方块，\n以便将{self.jailer}的号码传送给{self.prisoner}2。\n如果有卒，就消灭它；如果没有卒，就安装它。"
            case Lang.FR:
                return f"La personne jouant le rôle du {self.prisoner} 1 doit\nchanger une case sur l'échiquier afin que\nle {self.prisoner} 2 puisse révéler le numéro choisi\npar le {self.jailer}."
            case Lang.JA:
                return f'{self.prisoner}1は{self.jailer}の番号が{self.prisoner}2に伝わるように\nチェス盤のマスを1つ選択してください。\nポーンがあれば排除し、ポーンがなければ\n設置します。'
            case _:
                return f"The person playing the role of {self.prisoner} 1 should\nchange one square on the chessboard so that\nthe {self.prisoner} 2 can reveal the {self.jailer}'s chosen\nnumber."
    @property
    def prisoner1_log(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.prisoner}1对棋盘的状态做了一次改变。"
            case Lang.FR:
                return f"Le {self.prisoner} 1 a changé une des cases\nde l'échiquier."
            case Lang.JA:
                return f"{self.prisoner}1がチェス盤の状態を1箇所変更しました。"
            case _:
                return f"{self.prisoner}1 changed one of the squares\nin the chessboard."
    
    @property
    def prisoner2_instruction(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.prisoner}2应该从棋盘的状态猜出{self.jailer}的号码。"
            case Lang.FR:
                return f"La personne jouant le rôle du {self.prisoner} 2 doit\ndeviner le nombre fixé par le {self.jailer} à partir de l'état de l'échiquier."
            case Lang.JA:
                return f"{self.prisoner}2はチェス盤の状態から\n{self.jailer}の数字を当ててください。"
            case _:
                return f"The person playing the role of the {self.prisoner} 2\nshould guess the number set by the {self.jailer}\nfrom the state of the chessboard."
    
    @property
    def prisoners_victory(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"正确的! {self.prisoner}们赢了!"
            case Lang.FR:
                return f"Félicitations ! Les {self.prisoner}s ont gagné !"
            case Lang.JA:
                return f"正解です！{self.prisoner}の勝利！！"
            case _:
                return f"Congratulations! {self.prisoner}s win!"
    
    @property
    def random(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "随机排列"
            case Lang.FR:
                return "Au Hasard"
            case Lang.JA:
                return "ランダム配置"
            case _:
                return "Random"
    
    def result(self, winner: str) -> str:
        match self.lang:
            case Lang.CHI:
                return f"结果：{winner}获胜"
            case Lang.FR:
                return f"Gagnant: {winner}"
            case Lang.JA:
                return f"結果: {winner}の勝利"
            case _:
                return f"Winner: {winner}"
    
    @property
    def result_of_xor(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "排他性分离的结果:"
            case Lang.FR:
                return "Les résultats de OU exclusif:"
            case Lang.JA:
                return "排他的論理和の結果:"
            case _:
                return "The results of exclusive or:"
    
    @property
    def secret_binary(self) -> str:
        match self.lang:
            case Lang.CHI:
                return f"{self.jailer}的数字的二进制表示:"
            case Lang.FR:
                return f"Représentation binaire du numéro choisi par le {self.jailer}:"
            case Lang.JA:
                return f"{self.jailer}の数字の2進数表現:"
            case _:
                return f"Binary representation of {self.jailer}'s chosen number:"
    
    @property
    def start(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "开始"
            case Lang.FR:
                return "Début"
            case Lang.JA:
                return "スタート"
            case _:
                return "Start" 
    
    def validation(self, max_num: int) -> str:
        match self.lang:
            case Lang.CHI:
                return f"输入1到{max_num}之间的整数!"
            case Lang.FR:
                return f"La valeur d'entrée doit être un nombre entier compris entre 1 et {max_num}!"
            case Lang.JA:
                return f"1以上{max_num}以下の整数を入力してください！"
            case _:
                return f"Input value must be an integer between 1 and {max_num}!"
    
    @property
    def yes(self) -> str:
        match self.lang:
            case Lang.CHI:
                return "是"
            case Lang.FR:
                return "Oui"
            case Lang.JA:
                return "はい"
            case _:
                return "Yes"