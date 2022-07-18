#!/bin/bash
docker rm -f uscg_web_sweeper
docker build --tag=uscg_web_sweeper .
docker run -p 1337:1337 --rm --name=uscg_web_sweeper uscg_web_sweeper