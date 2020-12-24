#!/usr/bin/python3

from __future__ import unicode_literals
import random 
import os
import configparser
import random
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from logging import info
#from module import func
app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot','channel_secret'))
lineNotify=config.get('line-bot','notify_URL')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
#說話，貼文功能
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    ####最火爆的貼文
    if event.message.text in{'@近幾篇火爆Der推文','@最火爆Der推文','@最新推文','@火爆的推文','新貼文','最新貼文'}:
        import setSQL
        List=setSQL.get_bang_article()
        sent_text = ""
        for a in List:
            sent_text += a[0] + "\n" + a[1] + "\n\n"
        if List:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sent_text))#輸出火爆貼文的title a[0]及火爆貼文的url a[1] 
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="目前沒有非常火爆的貼文"))#收訊息一個，傳訊息也要一個函數
    
    ####快速連接PTT money版
    if event.message.text in{"@ptt","@Ptt","@PTt","@PTT","@pTT","@ptT","@pTt","@PtT"}:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="PTT中最省錢的版，PTT money版\nhttps://www.ptt.cc/bbs/money/index.html"))
    
    if event.message.text =='@連結LINE Notify':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="精彩爆文絕不錯過!!!!\n"+lineNotify))#將自己的Notify機器人網址貼在這裡
    
    if event.message.text =='12':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="34"))

    if event.message.text in{'hi','HI','Hi','hI','@hi','@HI','@Hi','@hI'}:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="HI"))
    #罐頭回復
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="親。這庵聽不懂呀\n說不定你可以與我們聯絡"))
            

if __name__ == "__main__":
    app.run()
