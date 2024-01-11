#!/bin/bash

# Activate Pipenv environment
echo "Activating Pipenv environment..."
pipenv shell

# Install packages from requirements.txt
echo "Installing packages from requirements.txt..."
pipenv install -r ../requirements.txt

echo "Script completed."