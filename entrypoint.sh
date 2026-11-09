#!/bin/sh
set -eu
python -m unittest discover -s tests -v
python analyser.py
