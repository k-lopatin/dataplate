#!/bin/bash 

# Install all needed dependencies
sudo apt-get install pip3
sudo apt-get install rabbitmq-server

# Run all install scripts of submodules
submodule_dirs=`find ./ -depth -maxdepth 1 -type d ! -name '.*'`
for submodule_dir in $submodule_dirs
do
    cd $submodule_dir
    ./install.sh
    cd ..
done
