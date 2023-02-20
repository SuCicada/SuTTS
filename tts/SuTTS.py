import os.path
import sys

moegoe_module = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../moegoe")
print("moegoe_module", moegoe_module)
sys.path.append(moegoe_module)

import numpy
import cache
from tts.MoeTTS import MoeTTS
import sounddevice

CACHE_MODE = False


class SuTTS:
    def __init__(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))

        model = os.path.join(current_dir, "../models/model.pth")  # input('Path of a VITS model: ')
        config = os.path.join(current_dir, "../models/config.json")  # input('Path of a config file: ')

        self.cache = audio_cache.getCache()
        self.moe_tts = MoeTTS(model, config)

    def get_audio_direct(self, text: str, speaker_id: int):
        print("generating audio...", text)
        audio, sampling_rate = self.moe_tts.text_to_speech(text, speaker_id)
        # print(audio, sampling_rate)
        # sounddevice.play(audio, sampling_rate, blocking=True)

        return audio, sampling_rate

    def get_audio_with_cache(self, text: str, speaker_id: int):
        res = self.cache.get(text=text, speaker=speaker_id)
        if res is not None:
            byte_arr, sampling_rate = res['data'], res['sampling_rate']
            audio = numpy.frombuffer(byte_arr, dtype='float32')
        else:
            print("cache miss, generating audio...")
            audio, sampling_rate = self.moe_tts.text_to_speech(text, speaker_id)
            byte_arr = audio.tobytes()
            self.cache.save(text, speaker_id, sampling_rate, byte_arr)
        return audio, sampling_rate

    def get_audio(self, text: str, speaker_id: int)->(numpy.ndarray, int):
        return self.get_audio_with_cache(text, speaker_id) if CACHE_MODE \
            else self.get_audio_direct(text, speaker_id)

    def speak(self, text: str, speaker_id: int):
        audio, sampling_rate = self.get_audio(text, speaker_id)
        print("playing audio...")
        print(audio, sampling_rate)
        sounddevice.play(audio, sampling_rate, blocking=True)
