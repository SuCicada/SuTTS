import pickle

import numpy
import sounddevice
from flask import make_response, Flask, request
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
so_vits_svc = SoVitsSvcTTS()


class AudioParams(BaseModel):
    text: str
    speaker: int


@app.post("/audio/so_vits_svc")
def audio():
    params = request.json
    text = params['text']
    # params['speaker']
    print(text)
    sampling_rate, audio_data = so_vits_svc.get_audio(text)
    audio_data: numpy.ndarray = audio_data
    byte_data = pickle.dumps({
        "status": "ok",
        "audio": audio_data.tobytes(),
        "sampling_rate": sampling_rate
    })

    response = make_response(byte_data)

    # sounddevice.play(audio, sampling_rate, blocking=True)
    response.headers['Content-Type'] = 'application/octet-stream'
    return response


def main():
    app.run(port=7100, debug=True)

# def main():
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0",port=7100, reload=True)
# if __name__ == '__main__':
#     main()
