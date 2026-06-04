#!/bin/bash

# Create the virtual environment named FarmDog
python3 -m venv FarmDog

# Activate environment
source FarmDog/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found, skipping dependency installation."
fi

#Run the Python file
python3 "FarmDog.py"

read
