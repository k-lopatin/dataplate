#!/usr/bin/env bash

# run linter, tests for collector

pylint3 modules
cd ..
coverage run --source=. -m unittest collector.modules.github.tests.search
coverage report -m