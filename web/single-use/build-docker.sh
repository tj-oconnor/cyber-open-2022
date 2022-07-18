#!/bin/bash
docker rm -f uscg_web_single_use
docker build --tag=uscg_web_single_use .
docker run -p 1337:1337 --rm --name=uscg_web_single_use uscg_web_single_use