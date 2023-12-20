#!/bin/bash

# Check if ufw is installed
if ! command -v ufw &> /dev/null; then
    echo "Installing ufw..."
    sudo apt-get update
    sudo apt-get install -y ufw
    echo "ufw has been installed."
else
    echo "ufw is already installed."
fi
