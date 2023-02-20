import pickle

import numpy
import requests
import sounddevice

text = """
おはようございます！何かお力になれることがあれば、おっしゃってください。
"""
req_json = {
    'text': text,
    'speaker': 2842,
}
response = requests.post('http://localhost:7100/audio/so_vits_svc', json=req_json)

json_data = pickle.loads(response.content)
# print(json_data)
audio = json_data['audio']
audio = numpy.frombuffer(audio, dtype=numpy.int16)
sampling_rate = json_data['sampling_rate']
print(audio, sampling_rate)
sounddevice.play(audio, sampling_rate, blocking=True)
