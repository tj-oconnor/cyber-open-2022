#!/bin/bash
docker rm -f uscg_web_wordy
docker build --tag=uscg_web_wordy .
docker run -p 1337:1337 --rm --name=uscg_web_wordy uscg_web_wordy