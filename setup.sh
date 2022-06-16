#!/bin/bash

set -x

# poetry init --python 3.10 --no-interaction

poetry config virtualenvs.in-project true
poetry env use ~/.pyenv/versions/3.10.5/bin/python
poetry install