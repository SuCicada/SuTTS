conda_env = su-tts
conda_run = conda run -n $(conda_env) --no-capture-output
run:
	python main.py
server:
	$(conda_run) python server.py

gradio:
	$(conda_run) python test/sovits_gradio.py


init_conda:
	conda env create -f environment.yml
	conda env list
install_requirements:
	pip install -r requirements.txt
	pip install -r repositories/so_vits_svc/requirements-infer.txt

download-model-moegoe:
	mkdir -p models
	cd models && \
	gdown "1PuUC_4cOvWFwOuskOapCk4VLaUXIgLPZ" -O model.pth && \
	gdown "1EGTJGwxIrjtyx6cJoF9-be5yw8YWV7OB" -O config.json

define wget_if_not_exist
	@if [ ! -f $(1) ]; then \
		mkdir -p $(dir $(1)); \
		wget -O $(1) $(2); \
	fi
endef
so_vits_svc_dir = repositories/so_vits_svc/
so_vits_svc_modules = $(so_vits_svc_dir)/_models
download-model-so_vits_svc:
	#@title 下载必要模型文件
	make -C $(so_vits_svc_dir) download-model-hubert
	mkdir -p $(so_vits_svc_modules)
	$(call wget_if_not_exist, $(so_vits_svc_modules)/mikisayaka/mikisayaka-G_50000-infer.pth ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/mikisayaka/mikisayaka-G_50000-infer.pth)
	$(call wget_if_not_exist, $(so_vits_svc_modules)/mikisayaka/mikisayaka-config.json ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/mikisayaka/mikisayaka-config.json)

	$(call wget_if_not_exist, $(so_vits_svc_modules)/sakurakyouko/sakurakyouko-G_100000-infer.pth ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/sakurakyouko/sakurakyouko-G_100000-infer.pth)
	$(call wget_if_not_exist, $(so_vits_svc_modules)/sakurakyouko/sakurakyouko-config.json ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/sakurakyouko/sakurakyouko-config.json)

git_update:
	#git pull
	git submodule update --recursive --remote

