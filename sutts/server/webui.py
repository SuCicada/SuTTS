# import json
# import pickle
#
# import numpy
# import requests
# import sounddevice
# from flask import Flask, render_template, request
# from flask_cors import CORS
#
# app = Flask(__name__)
# # CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=False)
# CORS(app)
# data = [
#     ('ギットハブ アクションのビルドが成功しました！'),
# ]
#
#
# @app.route('/speak', methods=['POST'])
# def speak():
#     params = request.json
#     print(params)
#     req_json = {
#         'text': params['text'],
#         'speaker': 2842,
#     }
#     response = requests.post('http://localhost:7100/audio', json=req_json)
#
#     json_data = pickle.loads(response.content)
#     # print(json_data)
#     audio = json_data['audio']
#     audio = numpy.frombuffer(audio, dtype='float32')
#     sampling_rate = json_data['sampling_rate']
#     print(sampling_rate)
#     sounddevice.play(audio, sampling_rate, blocking=True)
#
#     # data = response
#     # return data
#
#
# @app.route('/')
# def index():
#     return render_template('index.html', data=data)  # htmlのdata変数に辞書を渡す
#
#
# def main():
#     app.run(port=7000, debug=True)
