#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Check if auditd service is enabled
if systemctl is-enabled auditd &> /dev/null; then
    echo "auditd service is already enabled."
else
    # Enable auditd service
    systemctl enable auditd

    # Check if the enabling was successful
    if [ $? -eq 0 ]; then
        echo "auditd service has been enabled successfully."
        # Restart the service to apply changes
        systemctl restart auditd
    else
        echo "Failed to enable auditd service."
        exit 1
    fi
fi

