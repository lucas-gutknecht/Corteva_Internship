#!/bin/bash
cd /app

python3 -m venv venv
source ./venv/bin/activate

pip install -r docker/requirements.txt
python3 sqlite/database_commands.py
python3 flask/weather_app.py
