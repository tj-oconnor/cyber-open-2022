# Layers

A CTFd compatible docker image for a web challenge. Scenario: The website for Dot's Onion Farm has been hacked and defaced by a malicious group espousing the supremacy of garlic over onions as a cooking ingredient.

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

When the player visits the website, they see a manifesto along with a link to join the garlic gang. When they visit the link, they are denied entry but are left with a strange string of characters. Clever players will realize this is a .onion site and can connect to the address via a Tor browser. When they do, and return to the same "join" page, they are given the flag.

