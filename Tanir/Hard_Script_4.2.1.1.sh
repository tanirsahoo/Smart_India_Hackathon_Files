#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Check if rsyslog is installed
if command -v rsyslogd &> /dev/null; then
    echo "rsyslog is already installed."
else
    # Install rsyslog
    apt-get update
    apt-get install -y rsyslog

    # Check if the installation was successful
    if [ $? -eq 0 ]; then
        echo "rsyslog has been installed successfully."
    else
        echo "Failed to install rsyslog. Please check your internet connection and try again."
        exit 1
    fi
fi

