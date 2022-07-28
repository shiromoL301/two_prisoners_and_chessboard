from .patterns import Lang, Player, PlayersName

class GuideText:
    def __init__(self, lang: Lang=Lang.JPN, players_name: PlayersName=PlayersName.JAIL_PRISON):
        self.lang = lang
        self.players_name = players_name
    
    @property
    def all(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "全部"
            case Lang.FRA:
                return "Tous"
            case Lang.ITA:
                return "Tutti"
            case Lang.JPN:
                return "全配置"
            case _:
                return "All"
    
    def answer_by_prisoner2(self, answer: int) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.prisoner}2提交的答案是{answer}。"
            case Lang.FRA:
                return f"La réponse soumise par le {self.prisoner} 2\nest ``{answer}''"
            case Lang.ITA:
                return f"La risposta fornita dal {self.prisoner} 2\nè ``{answer}''."
            case Lang.JPN:
                return f"{self.prisoner}2の回答は「{answer}」です。"
            case _:
                return f"The answer submitted by {self.prisoner} 2\nis ``{answer}''"
    
    @property
    def app_closed(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "关闭应用程序。"
            case Lang.FRA:
                return "Fermé l'application." 
            case Lang.ITA:
                return "Chiudere l'app."
            case Lang.JPN:
                return "アプリを終了しました。"
            case _:
                return "Closed the App."


    @property
    def board_after_flipped(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "变化后的棋盘状态:"
            case Lang.FRA:
                return "Échiquier après avoir été modifié:"
            case Lang.ITA:
                return "Scacchiera dopo essere stata modificata:"
            case Lang.JPN:
                return "変更後のチェス盤の状態:"
            case _:
                return "Board after flipped:"
    
    @property
    def board_from_jailer(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"从{self.jailer}那里收到棋盘:"
            case Lang.FRA:
                return f"Échiquier reçu de {self.jailer}:"
            case Lang.ITA:
                return f"Scacchiera ricevuta da {self.jailer}:"
            case Lang.JPN:
                return f"{self.jailer}が渡したチェス盤:"
            case _:
                return f"Chessboard received from {self.jailer}:"
    
    @property
    def board_parities(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "棋盘式奇偶校验位序列:"
            case Lang.FRA:
                return "Parités de l'échiquier:"
            case Lang.ITA:
                return "Parità della scacchiera:"
            case Lang.JPN:
                return "盤面のパリティ:"
            case _:
                return "Parities of the chessboard:"
    
    @property
    def clear(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "全部清除"
            case Lang.FRA:
                return "Clair"
            case Lang.ITA:
                return "Liberare"
            case Lang.JPN:
                return "クリア"
            case _:
                return "Clear"

    @property
    def confirmation_screen(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "确认屏幕"
            case Lang.FRA:
                return "Confirmation"
            case Lang.ITA:
                return "Conferma"
            case Lang.JPN:
                return "確認画面"
            case _:
                return "Confirmation"
    
    def confirm_placement_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHS:
                return f"你想在第{row}行第{col}列设置一个棋子吗？"
            case Lang.FRA:
                return f"Voulez-vous placer le pion dans la ligne {row}, colonne {col}?"
            case Lang.ITA:
                return f"Volete piazzare una pedina nella riga {row}, colonna {col}?"
            case Lang.JPN:
                return f"{row}行{col}列目にポーンを設置しますか？"
            case _:
                return f"Do you want to place pawn \nin row {row}, column {col}?"
    
    def confirm_removal_pawn_at(self, location) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHS:
                return f"移除第{row}行和第{col}行的棋子？"
            case Lang.FRA:
                return f"Voulez-vous retirer le pion de la ligne {row}, colonne {col}?"
            case Lang.ITA:
                return f"Si vuole rimuovere la pedina nella riga {row}, colonna {col}?"
            case Lang.JPN:
                return f"{row}行{col}列目のポーンを取り除きますか？"
            case _:
                return f"Do you want to remove pawn \nin row {row}, column {col}?"
    
    @property
    def confirm_result(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "检查结果"
            case Lang.FRA:
                return "Confirmez le résultat"
            case Lang.ITA:
                return "Confermare il risultato"
            case Lang.JPN:
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
            case Lang.CHS:
                return f"{self.jailer}选择的数字是'{secret}'。"
            case Lang.FRA:
                return f"Le numéro choisi par le {self.jailer} est le ``{secret}''."
            case Lang.ITA:
                return f"Il numero scelto dal {self.jailer} è ``{secret}''."
            case Lang.JPN:
                return f"{self.jailer}が選んだ数字は「{secret}」です。"
            case _:
                return f"The {self.jailer}'s chosen number is ``{secret}''." 
     
    @property
    def finish(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "结束"
            case Lang.FRA:
                return "Finition"
            case Lang.ITA:
                return "Finitura"
            case Lang.JPN:
                return "終了"
            case _:
                return "Finish"
    
    def flipped_square(self, location: tuple[int, int]) -> str:
        row = location[0] + 1
        col = location[1] + 1
        match self.lang:
            case Lang.CHS:
                return f"由{self.prisoner}1修改的广场：第{row}行，第{col}列。"
            case Lang.FRA:
                return f"Carré retourné par le {self.prisoner} 1 : ligne {row}, colonne {col}."
            case Lang.ITA:
                return f"Quadrato capovolto dal {self.prisoner} 1: riga {row}, colonna {col}"
            case Lang.JPN:
                return f"{self.prisoner}1が変更したマス: {row}行{col}列目"
            case _:
                return f"Flipped Square by {self.prisoner} 1: row {row}, column {col}"
    
    @property
    def game_title(self) -> str:
        match self.lang:
            case Lang.CHS:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "有两个年轻女孩和一个棋盘的房间"
                    case PlayersName.DLR_CHL:
                        return "两个挑战者和一个棋盘问题"
                    case _:
                        return "两个囚犯和棋盘问题"
            case Lang.FRA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Chambre avec deux petites filles et un échiquier."
                    case PlayersName.DLR_CHL:
                        return "Problème d'échiquier avec deux challengers."
                    case _:
                        return "Deux prisonniers et un problème d'échiquier"
            case Lang.ITA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Camera con due bambine e una scacchiera"
                    case PlayersName.DLR_CHL:
                        return "Problema della scacchiera con due sfidanti"
                    case _:
                        return "Due prigionieri e una scacchiera"
            case Lang.JPN:
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
            case Lang.CHS:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "魔鬼"
                    case PlayersName.DLR_CHL:
                        return "经销商"
                    case _:
                        return "狱卒"
            case Lang.FRA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Diable"
                    case PlayersName.DLR_CHL:
                        return "Croupier"
                    case _:
                        return "Geôlier"
            case Lang.ITA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Diavolo"
                    case PlayersName.DLR_CHL:
                        return "Croupier"
                    case _:
                        return "Carceriere"
            case Lang.JPN:
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
            case Lang.CHS:
                return f"{self.jailer}放置棋子并选择1至{max_num}之间的任何数字。"
            case Lang.FRA:
                return f"La personne jouant le rôle du {self.jailer} doit placer\nle pion et choisir un nombre\nquelconque de 1 à {max_num}."
            case Lang.ITA:
                return f"La persona che interpreta il ruolo del {self.jailer}\ndeve piazzare la pedina e scegliere\nun numero qualsiasi da 1 a {max_num}."
            case Lang.JPN:
                return f'{self.jailer}はポーンを配置し、1～{max_num}のうち、\n好きな数字を選択してください。'
            case _:
                return f'The person playing the role of the {self.jailer} should\nplace the pawn and choose any number\nfrom 1 to {max_num}'
    
    @property
    def jailer_log(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.jailer}决定棋子的位置和数量。"
            case Lang.FRA:
                return f"Le {self.jailer} a déterminé le placement des pions\net un nombre secret."
            case Lang.ITA:
                return f"Il {self.jailer} determinava il posizionamento delle\npedine e un numero segreto."
            case Lang.JPN:
                return f"{self.jailer}がポーンの配置と数字を決定しました。"
            case _:
                return f"The {self.jailer} determined the placement of pawns\nand a secret number."
    
    @property
    def jailer_victory(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"不正确! {self.jailer}们赢了!"
            case Lang.FRA:
                return f"Échec de la mission ! Le {self.jailer} gagne!"
            case Lang.ITA:
                return f"Missione fallita! Il {self.jailer} vince!"
            case Lang.JPN:
                return f"不正解です！{self.jailer}の勝利！！"
            case _:
                return f"Mission failure! The {self.jailer} wins!"
    
    @property
    def next(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "下一步"
            case Lang.FRA:
                return "Suivant"
            case Lang.ITA:
                return "Successiva"
            case Lang.JPN:
                return "次へ"
            case _:
                return "Next"
    
    @property
    def no(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "不是"
            case Lang.FRA:
                return "Non"
            case Lang.ITA:
                return "No"
            case Lang.JPN:
                return "いいえ"
            case _:
                return "No"
    
    @property
    def number_from_jailer(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.jailer}选择的数字:"
            case Lang.FRA:
                return f"Numéro choisi par le {self.jailer}:"
            case Lang.ITA:
                return f"Numero scelto dal {self.jailer}:"
            case Lang.JPN:
                return f"{self.jailer}が選択した数字:"
            case _:
                return f"Number chosen by {self.jailer}:"
    
    @property
    def number_from_prisoner2(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.prisoner}2选择的数字:"
            case Lang.FRA:
                return f"Numéro choisi par le {self.prisoner} 2."
            case Lang.ITA:
                return f"Numero scelto dal {self.prisoner} 2:"
            case Lang.JPN:
                return f"{self.prisoner}2が選択した数字:"
            case _:
                return f"Number chosen by {self.prisoner}2"
    
    @property
    def ok(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "决定"
            case Lang.FRA:
                return "OK"
            case Lang.ITA:
                return "OK"
            case Lang.JPN:
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
            case Lang.CHS:
                return f"[{pname}的转变]"
            case Lang.FRA:
                return f"Phase de {pname}"
            case Lang.ITA:
                return f"[Fase del {pname}]"
            case Lang.JPN:
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
            case Lang.CHS:
                return "[播放器设置]"
            case Lang.FRA:
                return "[Paramètres du joueur]"
            case Lang.ITA:
                return "[Impostazioni del giocatore]"
            case Lang.JPN:
                return "【プレイヤー設定】"
            case _:
                return "[Player Settings]"

    @property
    def prisoner(self) -> str:
        match self.lang:
            case Lang.CHS:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "小女孩"
                    case PlayersName.DLR_CHL:
                        return "挑战者"
                    case _:
                        return "囚犯"
            case Lang.FRA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Petite Fille"
                    case PlayersName.DLR_CHL:
                        return "Challenger"
                    case _:
                        return "Prisonnier"
            case Lang.ITA:
                match self.players_name:
                    case PlayersName.DEVIL_GIRL:
                        return "Bambina"
                    case PlayersName.DLR_CHL:
                        return "Challenger"
                    case _:
                        return "Prigioniero"
            case Lang.JPN:
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
            case Lang.CHS:
                return f"{self.prisoner}1应该在棋盘上选择一个方块，\n以便将{self.jailer}的号码传送给{self.prisoner}2。\n如果有卒，就消灭它；如果没有卒，就安装它。"
            case Lang.FRA:
                return f"La personne jouant le rôle du {self.prisoner} 1 doit\nchanger une case sur l'échiquier afin que\nle {self.prisoner} 2 puisse révéler le numéro choisi\npar le {self.jailer}."
            case Lang.ITA:
                return f"La persona che interpreta il ruolo del {self.prisoner} 1\ndeve cambiare una casella della scacchiera\nin modo che il {self.prisoner} 2 possa rivelare il numero\nscelto dal {self.jailer}."
            case Lang.JPN:
                return f'{self.prisoner}1は{self.jailer}の番号が{self.prisoner}2に伝わるように\nチェス盤のマスを1つ選択してください。\nポーンがあれば排除し、ポーンがなければ\n設置します。'
            case _:
                return f"The person playing the role of {self.prisoner} 1 should\nchange one square on the chessboard so that\nthe {self.prisoner} 2 can reveal the {self.jailer}'s chosen\nnumber."
    @property
    def prisoner1_log(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.prisoner}1对棋盘的状态做了一次改变。"
            case Lang.FRA:
                return f"Le {self.prisoner} 1 a changé une des cases\nde l'échiquier."
            case Lang.ITA:
                return f"Il {self.prisoner} 1 ha cambiato una delle\ncaselle della scacchiera."
            case Lang.JPN:
                return f"{self.prisoner}1がチェス盤の状態を1箇所変更しました。"
            case _:
                return f"{self.prisoner}1 changed one of the squares\nin the chessboard."
    
    @property
    def prisoner2_instruction(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.prisoner}2应该从棋盘的状态猜出{self.jailer}的号码。"
            case Lang.FRA:
                return f"La personne jouant le rôle du {self.prisoner} 2 doit\ndeviner le nombre fixé par le {self.jailer} à partir de l'état de l'échiquier."
            case Lang.ITA:
                return f"La persona che interpreta il ruolo del {self.prisoner} 2\ndeve indovinare il numero stabilito dal\n{self.jailer} in base allo stato della scacchiera."
            case Lang.JPN:
                return f"{self.prisoner}2はチェス盤の状態から\n{self.jailer}の数字を当ててください。"
            case _:
                return f"The person playing the role of the {self.prisoner} 2\nshould guess the number set by the {self.jailer}\nfrom the state of the chessboard."
    
    @property
    def prisoners_victory(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"正确的! {self.prisoner}们赢了!"
            case Lang.FRA:
                return f"Félicitations ! Les {self.prisoner}s ont gagné !"
            case Lang.ITA:
                return f"Congratulazioni! I {self.prisoner} hanno vinto!"
            case Lang.JPN:
                return f"正解です！{self.prisoner}の勝利！！"
            case _:
                return f"Congratulations! {self.prisoner}s win!"
    
    @property
    def random(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "随机排列"
            case Lang.FRA:
                return "Au Hasard"
            case Lang.ITA:
                return "Casuale"
            case Lang.JPN:
                return "ランダム配置"
            case _:
                return "Random"
    
    def result(self, winner: str) -> str:
        match self.lang:
            case Lang.CHS:
                return f"结果：{winner}获胜"
            case Lang.FRA:
                return f"Gagnant: {winner}"
            case Lang.ITA:
                return f"Vincitore: {winner}"
            case Lang.JPN:
                return f"結果: {winner}の勝利"
            case _:
                return f"Winner: {winner}"
    
    @property
    def result_of_xor(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "排他性分离的结果:"
            case Lang.FRA:
                return "Les résultats de OU exclusif:"
            case Lang.ITA:
                return "I risultati dell'esclusiva o:"
            case Lang.JPN:
                return "排他的論理和の結果:"
            case _:
                return "The results of exclusive or:"
    
    @property
    def secret_binary(self) -> str:
        match self.lang:
            case Lang.CHS:
                return f"{self.jailer}的数字的二进制表示:"
            case Lang.FRA:
                return f"Représentation binaire du numéro choisi par le {self.jailer}:"
            case Lang.ITA:
                return f"Rappresentazione binaria del numero scelto dal {self.jailer}:"
            case Lang.JPN:
                return f"{self.jailer}の数字の2進数表現:"
            case _:
                return f"Binary representation of {self.jailer}'s chosen number:"
    
    @property
    def start(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "开始"
            case Lang.FRA:
                return "Début"
            case Lang.ITA:
                return "Inizio"
            case Lang.JPN:
                return "スタート"
            case _:
                return "Start" 
    
    def validation(self, max_num: int) -> str:
        match self.lang:
            case Lang.CHS:
                return f"输入1到{max_num}之间的整数!"
            case Lang.FRA:
                return f"La valeur d'entrée doit être un nombre entier compris entre 1 et {max_num}!"
            case Lang.ITA:
                return f"Il valore di ingresso deve essere un numero intero compreso tra 1 e {max_num}!"
            case Lang.JPN:
                return f"1以上{max_num}以下の整数を入力してください！"
            case _:
                return f"Input value must be an integer between 1 and {max_num}!"
    
    @property
    def yes(self) -> str:
        match self.lang:
            case Lang.CHS:
                return "是"
            case Lang.FRA:
                return "Oui"
            case Lang.ITA:
                return "Sì"
            case Lang.JPN:
                return "はい"
            case _:
                return "Yes"