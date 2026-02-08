# DLS Course semester 1 project: CLIP-Guided Domain Adaptation of Image Generators

Данный репозиторий является реализацией финального проекта курса https://dls.samcs.ru/part1.

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

### Summary
В целом подход описанный в статье https://arxiv.org/pdf/2108.00946 позволяет сдвигать генерацию в нужную сторону с помощью промпта. Таким образом получая модель которая генерирует изображения в нужном стиле. В самом базовом виде когда оптимизируется только Direction результат получается плохой потому что в процессе оптимизации все веса сдвигаются в сторону текстового промпта, таким образом помимо нужных фичей изменяются например яркость, фон и так далее, поэтому для достижения лучшего результата можно добавить регуляризацию,которая не дает так сильно меняться фичам и сохраняет ключевые черты в процессе оптимизации, например LPIPS, L2 норму весов. Так же подход когда вместо одного текстового промпта используется среднее промптов полученное с помощью разных шаблонов дает более точное направление для изменения что положительно сказывается на результате. Подход с обучением не всех слоев ускоряет обучение, но для каждого промпта приходится регулировать количество слоев для обучения, более сложные преобразования требуют большего количества обучающих слоев.