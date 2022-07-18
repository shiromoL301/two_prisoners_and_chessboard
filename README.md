# two_prisoners_and_chess_board

2人の囚人とチェス盤問題のシミュレーション

## シミュレーションの実行方法

Nixを用いた環境構築が終了していることを前提としています。
以下のコマンドで、環境に入ります。

```
nix develop path:$PWD
```

以下のコマンドでプログラムを実行します。

```
python main.py
```

## 遊び方

基本的にはGUIに表示される指示に従うだけです。
`config.py`に設定を記述して、言語やテーマを変更することができます。

## Nixを用いた環境構築

Windowsを使っている方は、まずWSLを導入します。
主目的ではないので、WSLが何であるかの説明は省略します。

#### WSLの導入(Windowsを使っている人)

スタートメニューの検索ボックスに「PowerShell」と入力し、「`Windows PowerShell`」を
**管理者権限で**実行し、出てきた画面に以下の行を入力し、Enterキーを押します:
```
wsl --install
```
次に、以下を実行します:
```
wsl -l -o
```
この結果に出てくる`Ubuntu-xx.xx`をインストールします。
執筆段階では、`Ubuntu-20.04`が最新であるため、これを以下のコマンドでインストールします:
```
wsl --install -d Ubuntu-20.04
```
これを実行した後、PCを再起動してください。

#### Nix、Nix Flakeのインストール

OSごとにインストール方法が異なるので、自身がお使いのOSの説明を参照してください。

#### Mac

ターミナルを起動し、以下を実行する:
```
sh <(curl -L https://nixos.org/nix/install) --darwin-use-unencrypted-nix-store-volume --daemon
```
これで上手くいかない場合は、以下を実行する:
```
sh <(curl https://abathur-nix-install-tests.cachix.org/serve/yihf8zbs0jwph2rs9qfh80dnilijxdi2/install) --tarball-url-prefix https://abathur-nix-install-tests.cachix.org/serve
```

`~/.config/nix/nix.conf`を作成し、ファイル内に以下を記述する:
```
experimental-features = nix-command flakes
```

Nix Flakeをインストールする:
```
nix-env -iA nixpkgs.nixFlakes
```

#### Linux

ターミナルを起動して、以下のコマンドで依存関係をインストールする:
```
sudo apt update
sudo apt upgrade
sudo apt install git curl make -y
```
Nixのインストール:
```
curl -L https://nixos.org/nix/install | sh
```
VimやEmacsなどお好きなエディタで、`~/.bashrc`に以下を記述する:
```
. ~/.nix-profile/etc/profile.d/nix.sh
```
その他のインストール方法は[公式ドキュメント](https://nixos.org/download.html)を参照。

`~/.config/nix/nix.conf`を作成し、ファイル内に以下を記述する:
```
experimental-features = nix-command flakes
```
Nix Flakeをインストールする:
```
nix-env -iA nixpkgs.nixFlakes
```

#### Windows(WSL)

WSLを利用します。導入がお済みでない場合は、前節を参照してWSLを導入してください。
依存関係のインストール:
```
sudo apt update
sudo apt upgrade
sudo apt install git curl make xdg-utils -y
```
`~/.bashrc`に以下を記述する:
```
PATH=$(/usr/bin/printenv PATH | /usr/bin/perl -ne 'print join(":", grep { !/\/mnt\/[a-z]/ } split(/:/));')
. ~/.nix-profile/etc/profile.d/nix.sh
```
Nix用のフォルダを作成:
```
sudo mkdir -p /etc/nix
```
`/etc/nix/nix.conf`を作成し、以下をファイル内に記述:
```
sandbox = false
use-sqlite-wal = false
experimental-features = nix-command flakes
```
Nixをインストールしたあと、環境を再読み込みし、Nix Flakeをインストールする:
```
curl -L https://nixos.org/nix/install | sh
source ~/.bashrc
nix-env -iA nixpkgs.nixFlakes
```

### Nixを用いたLaTeXファイルのビルド方法

以下のコマンドでLaTeXをビルドすることができる環境に入ることができます:
```
nix develop path:$PWD
```
(この操作は最初にLaTeX環境を作成するため、**初回はかなり時間が掛かります**。)

以下のコマンドで、`main.tex`ファイルがビルドされ、`result`フォルダ内に`main.pdf`ファイルが出力されます。
```
nix build path:$PWD
```