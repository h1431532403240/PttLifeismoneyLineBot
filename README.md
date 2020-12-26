# PttLifeismoneyLineBot
這是一個小小的side project，如果發現程式有問題，歡迎提交[Issues](https://github.com/h1431532403240/PttLifeismoneyLineBot/issues)

## 準備環境
目前自己的運行環境如下。

Linux raspberrypi 5.4.79

Python 3.7.3

Apache 2.4.38

MariaDB 10.3.27

PHP 7.3.19

phpMyAdmin 4.6.6deb5

ngrok 2.3.35

## 部屬步驟

自行建立一個資料庫，再從phpMyAdmin匯入```ptt_lifeismoney .sql```檔案

安裝Python套件

```
python pip install PyMySQL
python pip install requests
python pip install requests-html
python pip install beautifulsoup4
python pip install line-bot-sdk
python pip install django
python pip install flask
```

開啟ngrok

```
ngrok http -subdomain=自定義名稱 5000
ngrok http -subdomain=自定義名稱 5001
```

在目錄下設置config.ini檔案

```
[MySQL]
host = 預設為127.0.0.1
port = 預設為3306
user = 帳號
password = 密碼
db = 資料庫名稱

[line-bot]
channel_access_token = 你的channel_access_token
channel_secret = 你的channel_secret
notify_URL = https://notify-bot.line.me/oauth/authorize?response_type=code&scope=notify&response_mode=form_post&client_id=xxxxxxxxxxxxxxxxxxxx&redirect_uri=http://xxxxxxxx.ngrok.io/&state=f094a459-1d16-42d6-a709-c2b61ec53d60

[line-notify]
client_id = 你的notify id
client_secret = 你的notify secret
redirect_uri = ngrok中要使用的網址
```
