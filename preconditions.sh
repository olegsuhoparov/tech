#!/bin/bash
pwd
sleep 2
if [ ! -d env ]
then
  python -m venv env
else
  pwd
  echo "The env already exist"
fi
source env/scripts/activate
pip install -r "requirements.txt"
sleep 10