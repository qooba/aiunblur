#!/bin/bash
cp -r ../src/app ./app
cp -r ../models ./models
docker build -t qooba/aiunblur:dev -f Dockerfile.dev .
docker build -t qooba/aiunblur .
rm -rf ./app ./models
