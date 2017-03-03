#!/usr/bin/env bash

# runs a command $1 in directories $2
function run_in_dirs {
    for dir in ${@:2} #iter starts from second argument
    do
        cd $dir
        $1
        cd ..
    done
}

# runs a command $1 in components
function run_for_components {
    component_dirs=`find ./ -depth -maxdepth 1 -type d ! -name '.*'`
    run_in_dirs $1 $component_dirs
}

# runs a command $1 in modules of component
function run_for_modules {
    component_dirs=`find ./modules -depth -maxdepth 1 -type d ! -name '.*'`
    run_in_dirs $1 $component_dirs
}
