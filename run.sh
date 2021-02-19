#!/bin/bash

docker run -it --gpus all --ulimit memlock=-1 --rm -p 8000:8000 --name aiunblur qooba/aiunblur

