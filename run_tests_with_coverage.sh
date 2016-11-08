#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/myproject/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests_myproject.xml
PYTHONPATH=. py.test --cov-report xml --cov=../myproject
PYTHONPATH=. py.test --cov-report html --cov=../myproject

