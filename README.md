# DLS Course semester 1 project: CLIP-Guided Domain Adaptation of Image Generators

![Demo](assets/demo.gif) 

## Run
```
# clone the repo
git clone --recurse-submodules https://github.com/WHO777/dls_course_sem1_project.git
git submodule 

# install deps
uv sync
```

### Train
```
# clone the repo
https://github.com/WHO777/dls_course_sem1_project.git

# download StyleGAN2 weights
uv run gdown https://drive.google.com/uc?id=1EM87UquaoQmk17Q8d5kYIAHqu0dkYqdT -O weights/

# install deps
uv sync

# run notebooks/train.ipynb
```

### Gradio Server
```
# download weights
uv run gdown https://drive.google.com/drive/folders/1AJPrtDFBpfgPQQj6f84KxVm7NGMMqHLD -O weights/ --folder

PYTHONPATH=stylegan2-pytorch uv run python3 -m src.gradio_server
```