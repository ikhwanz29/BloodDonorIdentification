#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r build_requirements.txt
pip install -r requirements.txt