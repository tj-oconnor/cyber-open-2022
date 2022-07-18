# Hidden Wisdom

## Description

This challenge takes advantage of differences in packet timing to hide the flag.

The base capture provided is captured from the login screen of an old MMORPG called Anarchy Online. Data is captured from the login screen and not actual gameplay to line up with the hint text, claiming that the user has been banned from the game.

The flag is encoded as binary ascii characters in the time delta between each packet. The encoding is as follows:

Time delta ~= 0.00000256s => NOP
Time delta ~= 0.1s => 0
Time delta ~= 0.3s => 1

The player will need to calculate the time difference between each packet in the provided capture and apply this encoding to find the key.

The flag appears exactly once in the provided capture.

## Solution

[solve-hidden.py](solve-hidden.py)

The flag hidden inside is: ``AskNotForWhomTheFloridaManHacksHeHacksForThee``

