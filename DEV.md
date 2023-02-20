```bash
conda env export > environment.yml


conda env create -f environment.yml

conda activate su-tts
```

```bash
git submodule add --branch master \
git@github.com:CyborgParadisum/MoeGoe.git repositories/moegoe

git submodule add --branch 32k_dev \
git@github.com:CyborgParadisum/so-vits-svc.git repositories/so_vits_svc


```
