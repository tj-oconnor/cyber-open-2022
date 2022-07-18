# Fun Facts

A CTFd compatible docker image for a web challenge. Scenario: A classic minesweeper clone with a twist.

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

The save/load functionality is vulnerable to RCE through insecure deserialization. The save files are python pickles that can be exploited to get the flag on the server.

