#!/bin/bash
docker rm -f uscg_web_layers
docker build --tag=uscg_web_layers .
docker run -p 1337:1337 --rm --name=uscg_web_layers uscg_web_layers