#! /usr/bin/env bash

docker build -t pix_admin_api .
docker run -p 5000:5000 pix_admin_api
