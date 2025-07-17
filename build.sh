#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input --ignore "todo/css/input.css"
python manage.py migrate
