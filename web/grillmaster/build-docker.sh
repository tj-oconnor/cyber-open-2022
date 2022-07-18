#!/bin/bash
docker rm -f uscg_web_grillmaster
docker build --tag=uscg_web_grillmaster .
docker run -p 1337:1337 --rm --name=uscg_web_grillmaster uscg_web_grillmaster