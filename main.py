import os.path
import sys

import numpy

import audio_cache

moegoe_module = os.path.join(os.path.abspath(os.path.dirname(__file__)), "moegoe")
print("moegoe_module", moegoe_module)
sys.path.append(moegoe_module)

from utils.tts import SuTTS
import sounddevice as sd

current_dir = os.path.abspath(os.path.dirname(__file__))

model = os.path.join(current_dir, "models", "model.pth")  # input('Path of a VITS model: ')
config = os.path.join(current_dir, "models", "config.json")  # input('Path of a config file: ')
"""
ギットハブ アクションのビルドが達成されました。
ギットハブアクションのビルドが完了しました！！！
"""
text = """
ギットハブ アクションのビルドが成功しました！
"""
# 2792 佐倉杏子
# 2842 美樹さやか
佐倉杏子 = 2792
美樹さやか = 2842

CACHE_MODE = False


def get_audio(text: str, speaker_id: int):
    print("generating audio...")
    audio, sampling_rate = suTTS.text_to_speech(text, speaker_id)
    return audio, sampling_rate


def get_audio_with_cache(text: str, speaker_id: int):
    res = cache.get(text=text, speaker=speaker_id)
    if res is not None:
        byte_arr, sampling_rate = res['data'], res['sampling_rate']
        audio = numpy.frombuffer(byte_arr, dtype='float32')
    else:
        print("cache miss, generating audio...")
        audio, sampling_rate = get_audio(text, speaker_id)
        byte_arr = audio.tobytes()
        cache.save(text, speaker_id, sampling_rate, byte_arr)
    return audio, sampling_rate


def speak(text: str, speaker_id: int):
    audio, sampling_rate = get_audio_with_cache(text, speaker_id) if CACHE_MODE \
        else get_audio(text, speaker_id)
    sd.play(audio, sampling_rate, blocking=True)


if __name__ == '__main__':
    cache = audio_cache.getCache()

    suTTS = SuTTS(model, config)
    speak(text, 美樹さやか)
    # audio, sampling_rate = suTTS.text_to_speech(佐倉杏子, text)
    # sd.play(audio, sampling_rate, blocking=True)
