#!/usr/bin/env bash

# run linter, tests for collector

pylint3 modules
cd ..
python3 -m unittest collector.modules.github.tests.search