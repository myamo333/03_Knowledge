# docker

## dockerとは
**コンテナ**仮想化技術を使って、
アプリケーションを開発・配置・実行するための隔離された環境を提供するツール  
<br>

### コンテナ
  - パソコンやサーバー上で隔離され、干渉されない環境。パソコン側の変更を受けない
  - ホストOS上で、Dockerが存在し、その上でコンテナが存在する
  - PC側のパソコンアップデートとかで、環境が汚されてしまうとかがない
  - 一つのホストOSで複数のコンテナを設置・共存させることが可能
  - また、お互いのコンテナが干渉することはない
  - 更に、コンテナを持ち出しすることが比較的用意。イメージやDockerファイルで持ち出しできる
<br>

### docker Desktopインストール
- https://docs.docker.com/get-docker/
<br>

### Dockerイメージとは

- コンテナの実行環境テンプレート
    イメージには、コンテナに必要なソフトウェア・環境変数・設定などの情報が入っている
    イメージ＝コンテナの型となるもの
    例えば、pythonを動かしたい場合、pythonを動かせる情報を保持したりする
<br>

- 配布＆コンテナ環境の再現が可能
  イメージは、変更不可な静的テンプレート。
  どの環境で実行しても同じコンテナ環境が再現できる
<br>

- イメージとコンテナの入手
  イメージレジストリ(dockerhubなど)、Dockerfileなど
  - [dockerhub](https://hub.docker.com/)
    Dockerイメージを登録・配布を可能なサイト
    特に指定しない場合、Dockerhubからベースのイメージをがダウンロードされる
    ubuntuのイメージ、python、hello-worldなどが存在している
    マイナーなdockerもあるので注意
<br>

- コンテナのライフサイクル
  - コンテナはイメージから作成される
  - コンテナのステータス　   `Created`　→　`Up`　→　`Exited`
    - Upでコマンド実行できる
<br>

### Dockerの基本操作
#### イメージをダウンロード・破棄する
**※Dockerコマンドには旧コマンドあり。現在も利用可能で挙動は同じ**
- イメージをダウンロードするコマンド
    ```sh
    $ docker image pull {イメージ名}
    $ docker image pull ubuntu #ubuntuのイメージをダウンロード
    $ docker image pull ubuntu:20.04 #20.04でVer指定でダウンロード
    ```
<br>

- ローカルマシンに存在するイメージ一覧を表示するコマンド
    ```sh
    $ docker image ls
    REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
    ubuntu        latest    07db2ffa22da   2 days ago      98.8MB
    ubuntu        20.04     3f7ada54560f   8 days ago      65.7MB
    #REPOSITORY イメージの名前
    #TAG イメージのVer. タグを指定してダウンロードすることが可能
    ```
<br>

- ローカルマシンに存在するイメージを削除するコマンド
    ```sh
    $ docker image rm (イメージ名)
    $ docker image rm {IMAGE ID} #こちらでも削除することが可能
    ```
#### コンテナの作成・実行
- イメージからコンテナを作成し起動するコマンド
  ```sh
  $ docker container run {イメージ名}
  ```
<br>

- ローカルマシンに存在するコンテナ一覧を表示するコマンド
  コマンドが実行されるとすぐ`Exited`になる
  ```sh
  $ docker container ls
  # -a オプションをつけることで、起動していないコンテナも表示される
  $ docker container ls
  # CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  $ docker container ls -a 
  # CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
  # d26d9f12b96b   hello-world   "/hello"   33 seconds ago   Exited (0) 33 seconds ago             sleepy_rubin
  ```
  <br>
  
  下記のようなコンテナは、`UP`で動き続けている
  ```sh
  $ docker cotainer nginx
  $ docker container ls
  # CONTAINER ID   IMAGE     COMMAND                   CREATED              STATUS              PORTS     NAMES
  # 90e270da6db1   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    epic_leavitt
  ```
<br>

#### コンテナを停止・再起動
- 起動中のコンテナを止めるコマンド
  ```sh
  $ docker container stop {CONTAINER ID}
  # $ docker container stop {NAMES}
  # 2024/04/26 13:53:26 [notice] 1#1: exit
  ```
  <br>

- コンテナを再起動する(`Up`にする)コマンド
  ```sh
  $ docker container restart {CONTAINER ID}
  # $ docker container restart {NAMES}
  # $ docker container logs {NAMES or CONTAINER ID} #実行ログを確認する
  ```
<br>

#### コンテナを破棄
- コンテナを破棄するコマンド
  `Exited`になっているコンテナのみに有効
    ```sh
    $ docker container rm {CONTAINER ID or NAMES}
    ```
<br>

### Dockerコンテナの操作と挙動の深堀り
#### bashとは？
- LinuxやMacなどのUnix系のOSで利用されるシェルの一種
- PC操作などはカーネルを通して操作されている(機械語で裏で動いているもの)
- シェルは、OS(カーネル)に対して、様々な操作ができるようになる
<br>

#### Ubuntu環境を使って操作してみる
- Ubuntu : Linuxの一種(CentOSとかもある)で、広く普及
- Ubuntuにはデフォルトコマンドとして、`bash`が実行される
- rootというユーザー名でbashを通じてゲストOSのubuntuのコンテナにアクセス
    ```sh
    $ docker container run -it ubuntu:20.04
    # root@037c23b23020:/# 
    # /# exit
    ```
  - `-i` : ターミナルからUbuntuの標準入力を可能にする
  - `-t` : コマンド実行の結果(見た目)をきれいな状態にする
<br>

#### コンテナ起動時に実行されるコマンドを変更する
- Dockerのイメージの詳細情報を確認するコマンド
  ```sh
  $ docker image inspect {イメージ名}
  # $ docker image inspect ubuntu:20.04
  ```
<br>

- 起動時に実行されるコマンドの変更
    ```sh
    $ docker container run -it {イメージ名} {実行したいコマンド名}
    # $ docker container run -it ubuntu:20.04 pwd #pwdという好きなコマンドを実行
    ```
<br>

#### 既存のコンテナにコマンドを実行させる

- `Uo`状態のコンテナに任意のコマンドを実行させるコマンド
  ```sh
  $ docker container exec {コンテナ名} {実行したいコマンド}
  # $ docker container exec -it {コンテナ名} {実行したいコマンド} #表示が整う
  # $ docker container exec -it {コンテナ名} bash #起動済みのコンテナにbash実行
   ```
<br>

#### コンテナに好きな名前をつける
- コンテナに好きな名前をつける
    ```sh
    $ docker container run --name {つけたい名前} {コンテナ名} 
    # $ docker cotainer run --name my_ubuntu ubuntu:20.04
    # CONTAINER ID   IMAGE          COMMAND                   CREATED             STATUS                         PORTS     NAMES
    # c82319d52966   ubuntu:20.04   "/bin/bash"               8 seconds ago       Exited (0) 7 seconds ago                 my_ubuntu
    ```
<br>

#### コンテナの整理に便利なコマンド
- 停止済みのコマンドを一括削除するコマンド
  ```sh
  $ docker container prune
  ```
<br>

- `exited`になったら破棄するコマンド
  コンテナは使い捨てが多く、`--rm`はよく使う
  ```sh
  $ docker container run --rm {コンテナ名}
  # $ docker container run --rm ubuntu:20.04
  ```
<br>

- `Up`になっているコンテナを直ちに削除するコマンド
  ```sh
  $ docker container rm -f {コンテナ名}
  # $ docker container rm -f stoic_jones
  ```
<br>

#### デタッチドモードとフォアグラウンドモード
- デタッチドモード
  バックグラウンドでコンテナを回すことができるコマンド
  bashのときはデタッチドモードを使うことはほとんどない
  コンテナである処理を回して、処理をバックグラウンドで回したい場合などに利用する
  ```sh
  docker container run -it -d {コンテナ名}
  ```
<br>

- デタッチドモードになっているコンテナに接続するコマンド
  ```sh
  $ docker container attach {CONTAINER ID}
  ```
<br>

### Dockerのイメージをカスタムしてみる
- 基本的に実務ではDocker FileからDockerイメージを作る
<br>

#### Dockerefileとは？
- カスタムされたイメージを作るための設計書
- なぜDockerfileが必要なのか？
  - DockerHubなどのイメージの多くは、最低限の機能しか入っておらず、カスタマイズが必要
  - ベースイメージをDockerHubなどからダウンロードして、自分好みのコンテナを作る
  - いくらコンテナをカスタマイズしてもコンテナは作り直すと元に戻る
  - そのため、コンテナのもとになるイメージをカスタムすることが必要

#### Dokcerfileからイメージを作成する
```sh
$ docker image build {ディレクトリパス}
# $ docker image build . #currentディレクトリ
# REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
# <none>        <none>    11942c233947   9 days ago      65.7MB

# $ docker image build -t my-image . #任意の名前をつける
# REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
# my-image      latest    11942c233947   9 days ago      65.7MB

# $ docker image build -t my-image:v1 .　#任意の名前をタグをつける
# REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
# my-image      v1        11942c233947   9 days ago      65.7MB
```
<br>

#### COPYで好きなファイルをイメージに配置する
```docker
COPY {追加元} {追加先}
# ディレクトリ単位で指定することも可能
```
<br>

### .dockerignoreを利用する
- Creditialとか重いファイルを除外したい場合など
```dockerfile
COPY ./my_dir /app
```

#### (例) Dockerfileの中身
```docker
# ubuntu:20.04でイメージを作成
FROM ubuntu:20.04

# Dockerfileによりイメージを作成した後、apt updateを実行
RUN apt update
# curlをインストール 
RUN apt install -y curl
``` 
- `-y`とは、デフォルトでyesで回答する
<br>

#### CMDでデフォルトコマンドを設定する
- コンテナ実行時のデフォルトコマンドを設定する
- Dockerfileで一度しか使えない
- 複数のCMDがあれば、最後のCMDが実行される
  ```docker
  CMD ["実行ファイル","パラメータ1","パラメータ2"]
  # CMD ["ls","-la"]
  ```
<br>

#### レイヤー構造とは？
- イメージレイヤー (読込専用)
  - イメージの変更差分がレイヤーとして保存される
  - レイヤーがどんどん積み重なっていくイメージ
    - CMD ["bash"]
    - COPY ./foo.txt .
    - RUN apt install -y curl
    - RUN apt update
    - (ベースイメージのレイヤー)
    ```sh
    $ Docker image history
    # コマンドにより、変更差分を確認できる
    ```
- コンテナレイヤー (書込み可能)
  - コンテナ上での変更が保存される
  - コンテナの変更点を入れていく
<br>

#### イメージレイヤーの容量を小さくする
- 一つ一つレイヤーに積み重ねる
  ```docker
  RUN apt update
  RUN apt install -y curl
  RUN apt install -y vim
  CMD ["bash"]
  ```
<br>

- 一つの層に一気にaptを乗せるイメージ
レイヤーが少ないほうが容量は小さくなる
  ```docker
  RUN apt update && apt install -y culr　vim
  CMD ["bash"]
  ```
<br>

#### ENVで環境変数を設定する
- 特定の環境変数を仕込みたい場合
- 本番用、プロダクション用とかを環境変数としてフラグとして持たせたりする
- １度に複数個の環境変数を設定することも可能
- イメージ作成時とコンテナ実行時。両方で有効な変数
- コンテナの中で、環境変数を変えながら実施する場合、ENVを利用する
  ```docker
  ENV hello="Hello World"
  # ENV {キー1}={値1} {キー2}={値2}
  ENV hoge=HOGEHOGE
  ```
<br>

#### ARGで任意の変数を扱う
- イメージを作成時に利用する変数を渡す
- イメージ作成時のみ有効な一時的な変数
- Docker buildするときだけ有効な変数で、Dockerfileの中だけで影響を閉じたい場合に利用する
  ```docker
  ARG {キー1}={デフォルト値}
  # ARG message
  # RUN echo $message > message.txt
  # CMD ["cat", "message.txt"]
  ```
<br>

#### WOTKFDIRで作業ディレクトリを変更する
- RUNやCMDなどの作業ディレクトリを指定する
(未設定時は、"/"が作業ディレクトリになっている)
- 作業者がログインするフォルダを変えたりする
  ```docker
  WORKDIR {ディレクトリパス}
  # RUN touch 1.txt
  # WORKDIR /app/my_dir
  # RUN touch 2.txt
  # WORKDIR ..
  # RUN touch 3.txt
  ```
<br>

### マルチステージビルド

#### マルチステージビルドとは
- ステージによって必要なソフトウェアは異なる
  - hello.c -> `コンパイル (gcc)` -> a.out -> `実行 (Linux)`
- 同じイメージを使いまわそうとするとイメージサイズが大きくなる
  - ステージごとに必要なソフトウェアが異なるため、1つのイメージ上でやろうとすると
    イメージのサイズが大きくなる
- マルチステージビルドを使うと、
  1つのDockerfileでステージごとの環境を分離し、必要なイメージだけを作れる
<br>

#### マルチステージビルドでイメージファイルを削減する
- 一つのイメージで実施
    ```docker
    FROM gcc:12.2.0

    WORKDIR /app
    COPY ./hello.c .
    RUN gcc hello.c
    CMD ["./a.out"]
    ```
- マルチステージビルド
  コンパイラ部分が入っていないので、イメージサイズが小さくなる
  ```docker
  FROM gcc:12.2.0 AS compiler

  WORKDIR /app
  COPY ./hello.c .
  RUN gcc hello.c

  FROM ubuntu:20.04
  WORKDIR /app
  # --from=compiler compilerというステージから/app/a.outを.にコピーする
  COPY --from=compiler /app/a.out .
  CMD ["./a.out"]
  ```
<br>

- 複数環境向けの管理を楽にする
  - 例えば、開発環境のみ処理と本番環境の処理を分けたい
  - Dockerfileを開発環境・本番環境で分ける？
    - 共通処理部が二重管理になる
    - ファイルが多くなり管理が煩雑になる
    - マルチステージビルとなら1つのDockerfileでわけることができる
  ```docker
  #Common
  FROM ubuntu:20.04 AS base
  RUN apt update
  CMD ["sh", "-c", "echo My name is $my_name"]

  #Dev -> TEST, Prod -> Bob
  FROM base AS development
  ENV my_name=TEST 

  FROM base AS production
  ENV my_name=Bob
  ```
  ```sh
  $ docker image build --target development .
  $ docker image build --target production .
  ```
<br>

### Dockerとストレージ
- イメージレイヤーとコンテナレイヤーがある
- コンテナレイヤーは、コンテナが削除されると削除される
- コンテナレイヤーを永続化する方法がある
  - ボリュームとバインドマウント
<br>

#### ボリューム
- ボリュームの概要
  - dockerが管理しているボリューム領域がある
  - 複数のコンテナからアクセスできる
  - 外付けのハードディスクのようなイメージ
<br>

- 新しいボリューム領域を作成する
  ```sh
  $ docker volume create {ボリューム名}
  ```
<br>

- ボリューム領域一覧を表示する
  ```sh
  $ docker volume ls
  # DRIVER    VOLUME NAME
  # local     my-volume
  ```
<br>

- 指定したボリューム領域の詳細情報を表示する
  - ホストOSから直接ボリューム領域にはアクセスできない
  ```sh
  $ docker volume inspect {ボリューム名}
  # $ docker volume inspect my-volume
  # [
  #  {
  #      "CreatedAt": "2024-04-27T08:12:56Z",
  #      "Driver": "local",
  #      "Labels": null,
  #      "Mountpoint": "/var/lib/docker/volumes/my-volume/#_data",
  #      "Name": "my-volume",
  #      "Options": null,
  #      "Scope": "local"
  #  }
  # ]
  ```
<br>

- 指定したボリューム領域を削除する
  ```sh
  $ docker volume rm {ボリューム名}
  ```
<br>

- ボリュームに接続しながらコンテナを起動する
  ```sh
  # 書き方の違いのみで、どちらも同じ
  $ docker container run -v {Vol名}:{コンテナ内絶対パス} {イメージ}
  $ docker container run --mount type=volume src={Vol名},dst={コンテナ内絶対パス} {イメージ}
  ```

#### バインドマウント
- ホストマシン側のディレクトリに対してマウントする
- ホストマシン側から変更することが可能
- 特定のファイルをホスト側とコンテナ側双方から読み書きしたい事があれば
- お気に入りのエディタで編集した後、そのフォルダをマウントするとかの使い方がある
<br>

- バインドマウントしながらコンテナを起動する
  ```sh
  # 書き方の違いのみで、どちらも同じ
  $ doker container run -v {ホスト絶対パス}:{コンテナ内絶対パス} {イメージ}
  $ docker container run --mount type=bind, src={ホスト絶対パス},dst={コンテナ内絶対パス} {イメージ}
  # $ docker container run -it -v /Users/yuhei/Desktop/docker/my-dir:/app ubuntu:20.04
  ```
  - TIPS
    - `$(pwd)/my-dir` = 今のパスを読み出して連結する

#### ボリュームとバインドマウントの使い分け
- ボリューム
  - 複数のコンテナ間でのデータ共有が可能：YES
  - ホストからデータアクセス可能：NO
  - ホストの環境に依存する：NO
- バインドマウント
  - 複数のコンテナ間でのデータ共有が可能：YES
  - ホストからデータアクセス可能：YES
  - ホストの環境に依存する：YES
<br>
- 基本的には、ボリュームを使うことを推奨されている
  - ホスト側の状況により、変わってしまう可能性があるため
  - データベースのコンテナでは、ボリュームがよく使われる
  - ボリューム領域にデータを入れることで、コンテナが止まっても、データを維持できる
- バインドマウントが適切なケースは、ホスト側からの共通データを開発し、実行をコンテナ側で実施するという場合
<br>

### コンテナと接続する
- ホストとコンテナのポートを紐づける
  ブラウザ -> コンテナ
  PORTをホストと接続していないとアクセスできない
- ポートとは？
  - IPアドレス＋ポート番号でアクセスすることができる
  - IPアドレスを指定することで、サーバーを特定することができる
<br>

#### ホストとコンテナのポートを紐づける
- `-p`によって、ホストマシンのポートをコンテナのポートに紐づける
  ```sh
  $ docker container run -p {ホスト側のポート}:{コンテナ側のポート} {イメージ}
  # $ docker container run -p 3000:80 nginx
  # $ docker container ls
  # CONTAINER ID   IMAGE     COMMAND                   CREATED              STATUS              PORTS                  NAMES
  # 38bd2741c30a   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:3000->80/tcp   distracted_goodall
  ```
#### Dockerネットワークとは
- コンテナ同士の通信を簡単にしたり、不要なコンテナ同士の通信を防ぐために隔離する
- Dockerネットワークの一覧を確認するコマンド
  ```sh
  $ docker network ls
  ```
<br>

#### ブリッジネットワークとは
- コンテナ同士を橋渡しするような役割
- 同じブリッジに接続されているもの同士は通信することができる
- 何も指定しない場合、`bridge`に接続される
<br>

- ネットワークの詳細情報を表示する
  ```sh
  $ docker network inspect {ネットワーク}
  ```
<br>

- 新しいネットワークを作成する
  ```sh
  $ docker network create {ネットワーク}
  ```
<br>

- 指定したネットワークに接続したコンテナを起動する
  ```sh
  $ docker container run --network {ネットワーク} {イメージ}
  # $ docker network create my-net
  # $ docker container run -itd --rm --name my-nginx-2 --network my-net nginx  
  ```
<br>

#### ブリッジネットワーク内で通信をする
- あらかじめ、IPアドレスを知る必要がある
- 構成
  - bridge
    - my-nginx-1
    - my-ubuntu-1
  - my-net
    - my-nginx-2
    - my-ubuntu-2
- 実行したコマンド例
  ```sh
  $ docker container exec -it my-ubuntu-1 bash
  # curl http://{IPアドレス}
  # htmlファイルが返ってくる
  ```
<br>

- ブリッジネットワーク内で通信する (名前解決)
  - コンテナ間通信をする際は、IPアドレスを知る必要がある
  - Dockerのコンテナを起動した際に、把握することができず、毎回調べ、変更するのは現実的ではない
  - そのため、コンテナ名 -> IPアドレスに変更する
  - ただし、デフォルトでつながる`bridge`には利用できない
  ```sh
  curl http://my-nginx-2
  # 下記は、bridgeにつながるコンテナなので、利用できない
  # curl http://my-nginx-1
  # curl: (6) Could not resolve host: my-nginx-1
  ```
<br>

- ネットワークを削除する
  ```sh
  $ docker network rm {ネットワーク}
  ```
<br>