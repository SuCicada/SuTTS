# SuTTS

HuggingFace Spaces: [![HuggingFace  Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/SuCicada/SuTTS)

Web App: [生きてください。](https://sucicada.github.io/sutts-homepage/)

Source of Web App: [SuCicada/SuTTS-web](https://github.com/SuCicada/SuTTS-web)

<br>

**This is a TTS server with anime character voice by https://github.com/CyborgParadisum/so-vits-svc**

### 目前成功训练模型：
- 美樹さやか
- 佐倉杏子

## 下一步最主要也是最关键的声音是：岩倉玲音！！！


## For dev
```bash
make init_conda
. ./active.sh
conda activate su-tts
make install_requirements
make download-model-so_vits_svc

```

```bash
make server PORT=6005
```
注意する： 
- [moetts] 毎回生成された音声は違います。


