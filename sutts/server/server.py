import io
import json
import pickle

import numpy
import numpy as np
import sounddevice
from flask import make_response, Flask, request
from flask_cors import CORS
from pydantic import BaseModel

from sutts.inference.so_vits_svc import SoVitsSvcTTS

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from typing import Dict, Any
#
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = Flask(__name__)
CORS(app)

so_vits_svc = SoVitsSvcTTS()


class AudioParams(BaseModel):
    text: str
    speaker: int


# @app.post("/audio/so_vits_svc/{id}")
# def audio_data(id):

@app.post("/audio/so_vits_svc")
def audio():
    params = request.json
    text = params['text'].strip()
    # params['speaker']
    print(text)
    sampling_rate, audio_data = so_vits_svc.get_audio(text)
    audio_data: numpy.ndarray = audio_data
    # byte_data = pickle.dumps({
    #     "status": "ok",
    #     "sampling_rate": sampling_rate
    # })
    # "audio": audio_data.tobytes(),
    response_data = {
        "status": "ok",
        "sampling_rate": sampling_rate
    }
    # byte_data = audio_data.tobytes()
    from scipy.io.wavfile import write
    with io.BytesIO() as wav_file:
        write(wav_file, sampling_rate, audio_data)
        byte_data = wav_file.getvalue()

    response = make_response(byte_data)
    # open("hello.wav", "wb").write(audio_data)
    # from scipy.io.wavfile import write
    # write("hello.wav", sampling_rate, audio_data)
    # sounddevice.play(audio, sampling_rate, blocking=True)
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers["Access-Control-Expose-Headers"] = "*"
    response.headers['Response-Data'] = json.dumps(response_data)
    return response


def main():
    app.run(port=7100, debug=False, threaded=False)

# def main():
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     main()
