import numpy
import sounddevice
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from typing import Dict, Any

from pydantic import BaseModel

from tts.SuTTS import SuTTS
import pickle

#
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

su_tts = SuTTS()
from flask import make_response, Flask, request

app = Flask(__name__)


class AudioParams(BaseModel):
    text: str
    speaker: int


@app.post("/audio")
def audio():
    params = request.json
    text, speaker = params['text'], params['speaker']
    print(text, speaker)
    audio, sampling_rate = su_tts.get_audio(text, speaker)
    # sounddevice.play(audio, sampling_rate, blocking=True)
    audio: numpy.ndarray = audio
    byte_data = pickle.dumps({
        "status": "ok",
        "audio": audio.tobytes(),
        "sampling_rate": sampling_rate
    })

    response = make_response(byte_data)
    response.headers['Content-Type'] = 'application/octet-stream'
    return response




def main():
    app.run(port=7100, debug=True)

# def main():
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
