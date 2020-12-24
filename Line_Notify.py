import os
from flask import Flask, request, redirect, abort, jsonify
import requests
import setSQL
import getTime

app = Flask(__name__)


config = configparser.ConfigParser()
config.read('config.ini')

client_id = (config.get('line-notify', 'client_id'))
client_secret = (config.get('line-notify', 'client_secret'))
redirect_uri = (config.get('line-notify', 'redirect_uri'))


@app.route("/callback", methods=['POST'])
def gettoken():
    url = 'https://notify-bot.line.me/oauth/token'
    data = {'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret,
            'code': request.form.get('code')}
    try:
        res = requests.post(url, data).json()
        access_token = res['access_token']
        setSQL.save_user_token(access_token)
        return 'OK'
    except Exception as e:
        abort(400, e)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
