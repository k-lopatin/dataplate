#!/usr/bin/env bash

# runs a command $1 in directories $2
function run_in_dirs {
    echo 1
    ls
    echo $1
    echo $2
    for dir in ${@:2} #iter starts from second argument
    do
        echo $dir
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
    echo 2
    ls
    component_dirs=`find ./modules -depth -maxdepth 1 -type d ! -name '.*'`
    run_in_dirs $1 $component_dirs
}
