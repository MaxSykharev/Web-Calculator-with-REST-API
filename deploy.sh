#!/bin/bash

temp_dir="temp"

project_dir="$temp_dir/lcc-mytsg"

if [ -d "$project_dir" ]; then
    cd "$project_dir" && \
    git pull
else
    mkdir -p "$temp_dir" && \
    cd "$temp_dir" && \
    git clone git@github.com:tsgdigitalservices/lcc-mytsg.git
fi

cd "$project_dir" && \
docker-compose down && \
docker-compose build && \
docker-compose up -d && \

cd ../.. && \
sudo rm -rf "$temp_dir"
