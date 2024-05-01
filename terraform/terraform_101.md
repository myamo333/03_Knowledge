# Terraform
## Terraformとは
- AWSなどでサーバー・ネットワークその他の構築をコード(Infrastructure as Code)するためのOSS
- HashiCorp社の製品の1つであり、HashiCorp社は他にもPacker, Vault, Consul, Nomadなどのツールを提供
- AWS以外にも、GCPやAzureなどにも対応したベンダー非依存のツール
- Terraformを使うときは、.tfという拡張子のファイルに、JSONに似たHCLという形式のコードを書く
- その後、terraformコマンドを使って、コードを元にインフラを構築する
<br>

## Infrastructure as Codeのツールの活用
- Infrastructure as Codeのツールを活用すると、自力でスクリプトを書くより少ないコード量で、保守しやすいインフラを構築可能
- インフラのコードはGitなどでVer.管理したり、変更時に差分を確認することも可能
- 環境構築の再現性やコードの保守性といった観点から、Terraform等のツールを使ってInfrastructure as Codeを実施することが多い
<br>

## AWSでのInfrastructure as Codeのツール
|ツール|特徴|
|----|----|
|HashiCorp Terraform|クラウドベンダー非依存のOSS<br>HCLという比較的簡単な言語で実装可能<br>小規模から大規模まで使いやすい|
|AWS CloudFormation|AWS公式のツール<br>JSONまたはYAML形式で実装<br>コード量が多いと管理が難しくなりやすい|
|AWS CDK (Cloud Development Kit)|AWS公式のツール<br>TypeScriptなどの言語で実装するため、プログラミングの知識が必要|

<br>

## terraformコマンドの実行環境
- Terraformを使うときは、コードを書いて、terraformコマンドを実行
- AWSの環境をTerraformで構築する場合、terraformコマンドを実行するマシンに、AWSにアクセスする権限が必要
- PCからAWSにアクセスするにはアクセスキーを払い出す必要があり、terraformコマンドに必要な強い権限を付与したアクセスキーを払い出すと、漏洩した場合に、AWSの様々な操作ができてしまう
<br>
