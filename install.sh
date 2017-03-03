#!/bin/bash

source functions.sh

# Install all needed dependencies
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install rabbitmq-server
sudo pip3 install pylint3

# Run all install scripts of submodules
run_for_components ./install.sh
