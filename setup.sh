#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip install flask
pip show flask
python app.py
