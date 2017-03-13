#!/bin/bash

source ../functions.sh

echo 3
ls

sudo pip3 install --upgrade -r requirements.txt
sudo pip3 install --upgrade -r modules/*/requirements.txt

run_for_modules `sudo chmod +x *.sh`
run_for_modules ./install.sh

sudo chmod +x *.sh