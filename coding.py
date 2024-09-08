#!/bin/bash

# Define the directory containing email files
EMAIL_DIR="./emails"

# Define the Python script for phishing detection
PYTHON_SCRIPT="./code.py"

# Check if email directory exists
if [ ! -d "$EMAIL_DIR" ]; then
  echo "Error: Directory $EMAIL_DIR does not exist."
  exit 1
fi

# Loop through email files in the directory
for email_file in "$EMAIL_DIR"/*.txt; do
  if [ -f "$email_file" ]; then
    echo "Analyzing $email_file..."
    python3 "$PYTHON_SCRIPT" "$email_file"
  else
    echo "No email files found in $EMAIL_DIR."
  fi
done
