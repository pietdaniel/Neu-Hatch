#!/bin/sh

. /hatch_venv/bin/activate && python runserver.py -h 0.0.0.0 -p 5000
