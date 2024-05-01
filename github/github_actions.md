# Github Actions
## 設定
- mainブランチにプルリクエストがあった場合、main.pyとsub.pyを実行するアクション
```yaml
name: Run Scripts

on:
  push:
    branches:
      - main

jobs:
  run_scripts:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt
          # もし必要な場合は、requirements.txtを作成し、必要なパッケージを追加します

      - name: Run main.py
        run: python main.py

      - name: Run sub.py
        run: python sub.py

```

## Githubアクションを通して、Dockerfileをビルドとデプロイ
- Chat GPTの出力のため、変更する必要あり
```yaml
name: Deploy Docker Container to AWS EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up AWS CLI
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: your-aws-region

      - name: Install Docker
        run: |
          sudo apt-get update
          sudo apt-get install -y docker.io

      - name: Build Docker image
        run: docker build -t your-image-name .

      - name: SSH into EC2 and start container
        uses: appleboy/ssh-action@master
        with:
          host: your-ec2-ip
          username: ec2-user
          key: ${{ secrets.EC2_SSH_PRIVATE_KEY }}
          port: 22
          script: |
            docker stop your-container-name || true
            docker rm your-container-name || true
            docker rmi your-image-name || true
            docker pull your-image-name:latest
            docker run -d --name your-container-name -p 80:80 your-image-name:latest
```