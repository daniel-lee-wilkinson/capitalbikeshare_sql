#!/bin/bash

echo "Running Ruff to fix lint issues..."
ruff check . --fix

echo "Running Black for formatting..."
black .

echo "Running Flake8 to check for remaining issues..."
flake8 .
