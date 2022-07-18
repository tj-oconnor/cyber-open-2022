#!/bin/bash
docker rm -f uscg_web_fun_facts
docker build --tag=uscg_web_fun_facts .
docker run -p 1337:1337 --rm --name=uscg_web_fun_facts uscg_web_fun_facts