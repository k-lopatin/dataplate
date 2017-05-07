#!/bin/bash

sudo apt-get install redis-server

sudo pip3 install --upgrade -r requirements.txt

sudo chmod +x *.sh

# set config folders in components writable
cd ..
sudo find ./ -name config -type d -print0 | sudo xargs -0 chmod 777 -R