# Webアプリ開発の流れ
## ソフトウェア開発の流れ
- 下記の流れを繰り返しながら開発を進め、要所要所でDockerを使っている
`開発環境構築` -> `開発` -> `コミット` -> `ビルド` -> `テスト` -> `デプロイ` ->
`　　　　　　実装開発 　　　　　　　` `　　　　　CI　　　　　` `　　CD　　` 
<br>

- Dockerを利用する箇所
  - `開発環境構築`
  - `開発`
  - `ビルド`
  - `テスト`
  - `デプロイ`
<br>

- 開発環境と本番環境の違いを比べる
  - 開発環境@ローカルマシン
  Webコンテナがapiコンテナのアドレスを知っている必要がある
  - 本番環境@AWS ECS
  WebコンテナはECSの機能によりapiコンテナのアドレスの把握は不要
  - NGINX
    - /apiで始まるリクエストはapiコンテナに転送などの設定ができる
    - リバースプロキシ
  - 本番環境ではReactで作られたUIリソースをNGINXにホストする
  - 