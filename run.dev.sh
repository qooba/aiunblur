#!/bin/bash

docker run -it --gpus all --ulimit memlock=-1 -p 8000:8000 --name unblurme --rm -v $(pwd)/src/app:/app -v $(pwd)/models:/models qooba/aiunblur:dev /bin/bash

