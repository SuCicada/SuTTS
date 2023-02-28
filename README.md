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


