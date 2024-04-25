#!/usr/bin/env bash

set -o errexit  # exit on error
pip install --upgrade pip
pip install -r requirements.txt
cd nn_map
python manage.py collectstatic --no-input
python manage.py migrate