import os
import sys

import gradio as gr


sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(sys.path)
# os.environ['PYTHONPATH'] = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print("PYTHONPATH", os.environ['PYTHONPATH'])
# os.environ['USE_CACHE_INFERENCE_AUDIO'] = "False"

from cache import CacheConfig
CacheConfig.USE_CACHE_INFERENCE_AUDIO = False
from sutts.inference import newSoVitsSvcTTS, CharacterModel


class VitsGradio:
    def __init__(self):
        self.so_vits_svc1 = newSoVitsSvcTTS(CharacterModel.mikisayaka)
        self.so_vits_svc2 = newSoVitsSvcTTS(CharacterModel.sakurakyouko)
        # self.so = VitsSvc()
        # self.lspk = []
        # self.modelPaths = []
        # for root,dirs,files in os.walk("checkpoints"):
        #     for dir in dirs:
        #         self.modelPaths.append(dir)
        with gr.Blocks() as self.Vits:
            with gr.Tab("VoiceConversion"):
                with gr.Row() as self.VoiceConversion:
                    with gr.Column():
                        with gr.Row():
                            with gr.Column():
                                # self.srcaudio = gr.Audio(label = "输入音频")
                                self.text = gr.Textbox(label="输入文本", lines=5)
                                self.btnVC = gr.Button("说话人转换")
                                # with gr.Column():
                                # self.dsid = gr.Dropdown(label = "目标角色", choices = self.lspk)
                                # self.tran = gr.Slider(label = "升降调", maximum = 60, minimum = -60, step = 1, value = 0)
                                # self.th = gr.Slider(label = "切片阈值", maximum = 32767, minimum = -32768, step = 0.1, value = -40)
                                # with gr.Column():
                                # with gr.Row():
                                self.VCOutputs = gr.Audio()
                                self.VCOutputs1 = gr.Audio()
                                self.VCOutputs2 = gr.Audio()
                # self.btnVC.click(self.so.inference, inputs=[self.srcaudio,self.dsid,self.tran,self.th], outputs=[self.VCOutputs])
                self.btnVC.click(self.get_audio, inputs=[self.text], outputs=[
                    self.VCOutputs,
                    self.VCOutputs1,
                    self.VCOutputs2,
                ])
            # with gr.Tab("SelectModel"):
            #     with gr.Column():
            #         modelstrs = gr.Dropdown(label = "模型", choices = self.modelPaths, value = self.modelPaths[0], type = "value")
            #         devicestrs = gr.Dropdown(label = "设备", choices = ["cpu","cuda"], value = "cpu", type = "value")
            #         btnMod = gr.Button("载入模型")
            #         btnMod.click(self.loadModel, inputs=[modelstrs,devicestrs], outputs = [self.dsid,self.VoiceConversion])

    def get_audio(self, text):
        res1 = self.so_vits_svc1.get_audio_with_origin(text)
        res2 = self.so_vits_svc2.get_audio_with_origin(text)
        return res1[0], res1[1], res2[1]


if __name__ == '__main__':
    grVits = VitsGradio()

    grVits.Vits.launch(debug=True)
# grVits.Vits.launch(debug=True,share=True)
