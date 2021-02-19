FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

WORKDIR /
RUN apt-get update && apt-get -yq install python3-pil
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install curl git cmake ack g++ tmux -yq

#RUN git clone https://github.com/fastai/fastai
#RUN pip3 install -e "fastai[dev]"

RUN git clone https://github.com/fastai/fastai1
RUN pip3 install -e "fastai1[dev]"

RUN pip3 install qdi fastapi uvicorn jinja2 aiofiles python-multipart
ENV PYTHONPATH="/app:${PYTHONPATH}"
WORKDIR /app
COPY ./app /app
COPY ./models /models

ENTRYPOINT [ "/bin/bash", "./start-reload.sh" ]
