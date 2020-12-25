import os
import requests
import setSQL

config = configparser.ConfigParser()
config.read('config.ini')

client_id = (config.get('line-notify', 'client_id'))
client_secret = (config.get('line-notify', 'client_secret'))


def push_text(token, List):
    accesstoken = token
    Line_Notify_Account = {'Client ID': client_id,
                           'Client Secret': client_secret,
                           'token': accesstoken}

    headers = {'Authorization': 'Bearer ' + Line_Notify_Account['token'],
               "Content-Type": "application/x-www-form-urlencoded"}

    params = {"message": "【爆文通知】\n" + List[0] + "\n" + List[1]}

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
