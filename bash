#!/bin/bash

# Update package list and install Python and pip
echo "Updating package list..."
sudo apt-get update

echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip

# Install necessary Python packages
echo "Installing Python packages..."
pip3 install -r requirements.txt

echo "Setup complete!"

