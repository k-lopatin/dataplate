#!/usr/bin/env bash

# runs a command $2 in directories $1
function run_in_dirs {
    for dir in $1
    do
        cd $dir
        $2
        cd ..
    done
}

# runs a command $1 in components
function run_for_components {
    component_dirs=`find ./ -depth -maxdepth 1 -type d ! -name '.*'`
    run_in_dirs $component_dirs $1
}

# runs a command $1 in modules of component
function run_for_modules {
    component_dirs=`find ./modules -depth -maxdepth 1 -type d ! -name '.*'`
    run_in_dirs $component_dirs $1
}