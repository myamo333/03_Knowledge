# DockerでStreamlitのWebアプリを動かす

## Docker Desktopのインストール
- [Docker Desktop公式サイト](https://www.docker.com/products/docker-desktop/)
<br>

## Dockerfileを作成
```docker
FROM python:3.9.19-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y upgrade && pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["./app/🏠_Home_Page.py"]
```
<br>

## Dockerfileからイメージをビルド
```sh
$ docker image build -t web-app:latest .
```
<br>

## Dockerイメージを確認
```sh
$ docker image ls
# REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
# web-app      latest    3ad61e8de3df   41 minutes ago   655MB
```

## DockerをRun
- ホスト側の443ポートをコンテナ側の8501ポートに接続する設定
```sh
$ docker container run -p 443:8501 web-app:latest 
```
## Streamlitへ接続
- http://lcalhost:443
- 現状、ローカルホストへの接続ができることは確認
- EC2インスタンスでコンテナ起動した場合、グローバルIPで接続できる
  http://EC２インスタンスのIPアドレス:443

## AWSでDockerでStremlitのWebアプリを動かす
### Dockerをインストール
- Dockerをインストール
    ```sh
    $ sudo yum install -y docker
    $ sudo systemctl start docker
    $ sudo usermod -a -G docker ec2-user
    ```
- 自動起動を有効にする
  ```sh
  $ sudo systemctl enable docker
  ```
<br>

### EC2に開発したスクリプトをフォルダごとアップロード
- githubのCI環境を使えるといいが、現状は、フォルダコピーがはやい
- フォルダコピー後は、上記のDockerイメージのビルドから実施する
```sh
$ scp -r -i {秘密鍵}.pem {アップロードするフォルダ} ec2-user@{パブリックIP}:/home/ec2-user
```
