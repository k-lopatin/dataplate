#!/bin/bash

source functions.sh

# Install all needed dependencies
sudo apt-get update
sudo apt-get install python3
yes Y | sudo apt-get install python3-pip
yes Y | sudo apt-get install rabbitmq-server
sudo pip3 install pylint

sudo chmod +x *.sh

# Run all install scripts of submodules
run_for_components ./install.sh
