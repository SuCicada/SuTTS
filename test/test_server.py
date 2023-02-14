import pickle

import numpy
import requests
import sounddevice

text = """
    ギットハブ アクションのビルドが成功しました！
    """
req_json = {
    'text': text,
    'speaker': 2842,
}
response = requests.post('http://localhost:7100/audio', json=req_json)

json_data = pickle.loads(response.content)
# print(json_data)
audio = json_data['audio']
audio = numpy.frombuffer(audio, dtype='float32')
sampling_rate = json_data['sampling_rate']
print(audio,sampling_rate)
sounddevice.play(audio, sampling_rate, blocking=True)
