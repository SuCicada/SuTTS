run:
	python main.py

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
modules_dir = repositories/so_vits_svc/_models
download-model-so_vits_svc:
	#@title 下载必要模型文件
	#make -C repositories/so_vits_svc download-model
	$(call wget_if_not_exist, hubert/hubert-soft-0d54a1f4.pt, https://github.com/bshall/hubert/releases/download/v0.1/hubert-soft-0d54a1f4.pt)
	mkdir -p $(modules_dir)
	$(call wget_if_not_exist, $(modules_dir)/mikisayaka/mikisayaka-G_50000-infer.pth ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/mikisayaka/mikisayaka-G_50000-infer.pth)
	$(call wget_if_not_exist, $(modules_dir)/mikisayaka/mikisayaka-config.json ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/mikisayaka/mikisayaka-config.json)

	$(call wget_if_not_exist, $(modules_dir)/sakurakyouko/sakurakyouko-G_100000-infer.pth ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/sakurakyouko/sakurakyouko-G_100000-infer.pth)
	$(call wget_if_not_exist, $(modules_dir)/sakurakyouko/sakurakyouko-config.json ,\
			https://huggingface.co/SuCicada/SuTTS/resolve/main/sakurakyouko/sakurakyouko-config.json)

git_update:
	#git pull
	git submodule update --recursive --remote

