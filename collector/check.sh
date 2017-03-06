#!/usr/bin/env bash

# run linter, tests for collector

pylint modules
cd ..
coverage run --source=. -m unittest collector.modules.github.tests.search collector.modules.github.tests.search
coverage report -m