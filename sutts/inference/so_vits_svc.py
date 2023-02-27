import io
import logging
import os
import sys
from io import BytesIO

import numpy
import numpy as np
from gtts import gTTS
from pydub import AudioSegment

from cache import newCache, CacheConfig
from sutts.inference import CharacterModel
from sutts.utils.path import add_dependencies, so_vits_svc_path

add_dependencies()
print(sys.path)

from repositories.so_vits_svc.inference.utils import SoVitsSvc

# so = VitsSvc()
# device = "cpu"
# so.set_device(device)
# so.loadCheckpoint("mikisayaka")
logging.getLogger("gtts").setLevel(logging.INFO)


# def get_audio_data(wav_bytes):
#     # Open the WAV file
#     # wav = "/Users/peng/PROGRAM/GitHub/MoeGoe/google/hello1.wav"
#     # with wave.open(wav, 'r') as wav_file:
#     #     # Get the sample rate
#     #     sample_rate = wav_file.getframerate()
#     # Get the number of frames
#     # num_frames = wav_file.getnframes()
#     # Read the data as a raw byte string
#     # data = wav_file.readframes(num_frames)
#     # Convert the data to a NumPy array
#     data = np.frombuffer(wav_bytes, dtype=np.int16)
#     # Return the sample rate and data as a tuple
#     return data

class SoVitsSvcTTS:
    # def __init__(self, model_path, config_path):
    def __init__(self, character_model: CharacterModel):
        self.cache = newCache()
        self.so = SoVitsSvc(character_model.model_path, character_model.config_path)
        self.speaker = character_model.speaker

    def mp3_to_wav(self, mp3_bytes):
        # mp3 to wav
        mp3 = AudioSegment.from_file(io.BytesIO(mp3_bytes), format="mp3")
        sampling_rate = mp3.frame_rate
        wav = io.BytesIO()
        mp3.export(wav, format="wav")
        wav_bytes = wav.getvalue()
        return sampling_rate, wav_bytes

    def text_to_wav(self, text):
        audio_obj = self.cache.get(text, "google")
        if not audio_obj:
            print("miss cache, get origin audio from google")
            stream = BytesIO()
            tts = gTTS(text, lang='ja', slow=False)
            tts.write_to_fp(stream)
            mp3_bytes = stream.getvalue()
            sampling_rate, wav_bytes = self.mp3_to_wav(mp3_bytes)
            self.cache.save(text, "google", sampling_rate, wav_bytes)
        else:
            sampling_rate, wav_bytes = audio_obj.sampling_rate, audio_obj.data
        return sampling_rate, wav_bytes

    # # get mp3
    # open("hello.mp3", "wb").write(mp3_bytes)
    # mp3_bytes = open("hello.mp3", "rb").read()

    # tmp = np.frombuffer(wav_bytes, dtype=np.int16)
    # sounddevice.play(tmp, sampling_rate, blocking=True)
    def transform_audio(self, text, _sampling_rate, wav_bytes):
        speaker = self.speaker

        def _transform_audio():
            audio_data = np.frombuffer(wav_bytes, dtype=np.int16)
            # audio_data = get_audio_data(wav_bytes)
            # print(srcaudio)
            # sampling_rate, audio = get_audio(srcaudio)
            srcaudio = (_sampling_rate, audio_data)
            chara = speaker  # "mikisayaka"  # 目标角色
            tran = 0  # 升降调
            slice_db = -40  # 切片阈值
            sampling_rate, audio = self.so.inference(srcaudio, chara, tran, slice_db)
            return sampling_rate, audio

        if CacheConfig.USE_CACHE_INFERENCE_AUDIO:
            audio_obj = self.cache.get(text, speaker)
            if not audio_obj:
                print("miss cache, inference audio")
                # inference
                sampling_rate, audio = _transform_audio()
                self.cache.save(text, speaker, sampling_rate, audio.tobytes())
            else:
                sampling_rate, byte_arr = audio_obj.sampling_rate, audio_obj.data
                audio = numpy.frombuffer(byte_arr, dtype=np.int16)
            return sampling_rate, audio
        else:
            return _transform_audio()

    def get_audio_with_origin(self, text) -> ((int, numpy.ndarray), (int, numpy.ndarray)):
        text = text.strip()
        orgin_sampling_rate, wav_bytes = self.text_to_wav(text)
        sampling_rate, audio = self.transform_audio(text, orgin_sampling_rate, wav_bytes)

        wav: numpy.ndarray = numpy.frombuffer(wav_bytes, dtype=np.int16)
        return (orgin_sampling_rate, wav), (sampling_rate, audio)

    # def main():
    def get_audio(self, text) -> (int, numpy.ndarray):
        ori, res = self.get_audio_with_origin(text)
        return res
        # sounddevice.play(np.frombuffer(wav_bytes, dtype=np.int16),
        #                  orgin_sampling_rate, blocking=True)
        # sounddevice.play(audio, sampling_rate, blocking=True)

# def main():
# app.run(port=7100, debug=True)

# def main():
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
