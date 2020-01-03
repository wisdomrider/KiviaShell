#!/usr/bin/env bash
# installing ai 
pip3 install rasa_nlu
pip3 install sklearn_crfsuite
pip3 install spacy
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
clear
echo "Training AI please wait sometime !"
BASEDIR=$(dirname "$0")
python3 -m rasa_nlu.train --config $BASEDIR/config_spacy.yml --data $BASEDIR/train.md --path $BASEDIR/projects


