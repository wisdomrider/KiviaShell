#!/usr/bin/env bash
#http://localhost:5000/parse?q=hi
#python3 -m rasa_nlu.train --config config_spacy.yml --data train.md --path projects
BASEDIR=$(dirname "$0")
python3 -m rasa_nlu.server --port 2847 --path $BASEDIR/projects
