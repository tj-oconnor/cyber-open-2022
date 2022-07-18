# Wordy

A CTFd compatible docker image for a web challenge. Scenario: A word guessing game that we are all familiar with in 2022. However, this one is stuck in hard mode and only allows you to make one guess. If you can correctly guess the word then you get a prize!

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

The app retains your previous game data and if you send the game ID of a previous game along with the correct word you got from that game, then you can "win" and get the flag. However, you have to do it quickly enough to beat the garbage collection.

