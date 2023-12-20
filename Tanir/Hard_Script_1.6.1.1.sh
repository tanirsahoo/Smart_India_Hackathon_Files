#!/bin/bash

# This script performs system hardening tasks for Ubuntu Desktop, including checking for and installing AppArmor

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Starting system hardening..."

# Check if AppArmor is installed
if dpkg -l | grep -q apparmor; then
    echo "AppArmor is already installed."
else
    echo "Installing AppArmor..."
    
    # Update package list
    apt-get update
    
    # Install AppArmor
    apt-get install -y apparmor
    
    echo "AppArmor installed."
fi

echo "System hardening complete."

