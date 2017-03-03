#!/bin/bash

source ../functions.sh

sudo pip3 install --upgrade -r requirements.txt
sudo pip3 install --upgrade -r modules/*/requirements.txt

sudo chmod +x *.sh