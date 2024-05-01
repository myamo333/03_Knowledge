# Docker Compose
- Spring boot
- Postgre SQL

## Docker Composeとは
- 多くのコマンドを一括で実行できるツール
- 複数のコンテナを設置して、Webアプリを作成するのが一般的
- 他人に同じ環境を共有するのが困難といった課題を解決する
<br>

- `docker-compose.yml`
  自分が作りたいdockerの設定をすべて記述する
  ```sh
  # yamlの設定どおりに、Dockerを立ち上げる
  $ docker compose up
  ```

- Docker Compose vs Docker command
  - Docker compoase
    ```sh
    $ docker compose up
    ```
    - yaml
        ```yml
        version: '3.9'
        services:
        api:
            build: ./api
            ports:
            - 8080:8080
        ```
  - Docker command 
    ```sh
    $ docker image build -t api-img ./api
    $ docker container run --name api -p 8080:8080 api-img
    ```
<br>

### 最終的なyaml
```yml
  version: '3.9'
  services:
    api:
      build: ./api
      ports:
        - 8080:8080
      depends_on:
        - db
    db:
      image: postgres:15
      ports:
        - 5432:5432
      environment:
        - POSTGRES_PASSWORD=mypassword
        - POSTGRES_USER=postgres
        - POSTGRES_DB=appdb
      volumes:
        - db-storage:/var/lib/postgresql/data
        - ./db/initdb:/docker-entrypoint-initdb.d

  volumes:
    db-storage:
  ```