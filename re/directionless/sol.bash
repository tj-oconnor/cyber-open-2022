#!/bin/bash

PARAMS="$(ltrace ./directionless 2>&1 | grep write | sed -e 's/write//' -e 's/).*$/),/')"
python3 -c "print(''.join(x[1] for x in sorted([$PARAMS])))"
