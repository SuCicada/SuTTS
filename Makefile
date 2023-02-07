run:
	python main.py

init_conda:
	conda env create -f environment.yml
	conda env list
install_requirements:
	pip install -r requirements.txt

download_model:
	mkdir -p models
	cd models && \
	gdown "1PuUC_4cOvWFwOuskOapCk4VLaUXIgLPZ" -O model.pth && \
	gdown "1EGTJGwxIrjtyx6cJoF9-be5yw8YWV7OB" -O config.json
