run:
	python main.py

init_conda:
	conda env create -f environment.yml
	conda env list
install_requirements:
	pip install -r requirements.txt
	pip install -r so-vits-svc/requirements-mac.txt

download-model-moegoe:
	mkdir -p models
	cd models && \
	gdown "1PuUC_4cOvWFwOuskOapCk4VLaUXIgLPZ" -O model.pth && \
	gdown "1EGTJGwxIrjtyx6cJoF9-be5yw8YWV7OB" -O config.json

download-model-so_vits_svc:
	#@title 下载必要模型文件
	make -C repositories/so_vits_svc download-model

git_update:
	#git pull
	git submodule update --recursive --remote

