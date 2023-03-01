# SuTTS

[![Hugging  Face  Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/SuCicada/SuTTS)

Web App: https://sucicada.github.io/sutts-homepage/

Source of Web App: https://github.com/SuCicada/SuTTS-web


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


