# Fun Facts

A CTFd compatible docker image for a web challenge. Scenario: A bored developer created a site that sends random fun facts using the new and exciting PushManager API that everyone seems so fond of. The only problem is, he got too bored and decided to go play video games and didn't finish the frontend. Can you find a way to finish his work and receive messages?

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

This is a coding challenge. With the provided VAPID Public Key, the user can implement their own service worker and push notification subscription. Once the subscription is complete, they can send the endpoint, keys, etc to the provided API and recieve the flag!

