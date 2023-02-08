import json
import pickle

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    ('ギットハブ アクションのビルドが成功しました！'),
]


@app.route('/speak', methods=['POST'])
def speak():
    params = request.json
    print(params)
    req_json={
        'text': params['text'],
        'speaker': 2842,
    }
    response = requests.post('http://localhost:7100/audio', json=req_json)

    json_data = pickle.loads(response.content)
    print(json_data)
    audio = json_data['audio']
    sampling_rate = json_data['sampling_rate']
    # data = response
    # return data


@app.route('/')
def index():
    return render_template('index.html', data=data)  # htmlのdata変数に辞書を渡す


def main():
    app.run(port=7000, debug=True)
