import os
import requests
import setSQL

config = configparser.ConfigParser()
config.read('config.ini')

client_id = (config.get('line-notify', 'client_id'))
client_secret = (config.get('line-notify', 'client_secret'))


def push_text():
    accesstoken = setSQL.get_alluser_token()
    Line_Notify_Account = {'Client ID': client_id,
                           'Client Secret': client_secret,
                           'token': accesstoken}

    headers = {'Authorization': 'Bearer ' + Line_Notify_Account['token'],
               "Content-Type": "application/x-www-form-urlencoded"}

    params = {"message": setSQL.auto_push_message()}

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)

    print(r.status_code)
