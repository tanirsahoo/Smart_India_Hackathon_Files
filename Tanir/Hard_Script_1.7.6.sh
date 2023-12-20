#!/bin/bash

# This script ensures proper permissions on /etc/issue.net

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Checking permissions on /etc/issue.net..."

# Define the correct permissions for /etc/issue.net (e.g., read-only for all)
correct_permissions="644"

# Get current permissions on /etc/issue.net
current_permissions=$(stat -c "%a" /etc/issue.net 2>/dev/null)

if [[ -n "$current_permissions" ]]; then
    if [ "$current_permissions" != "$correct_permissions" ]; then
        echo "Updating permissions on /etc/issue.net..."
        
        # Set correct permissions
        chmod $correct_permissions /etc/issue.net

        echo "Permissions updated."
    else
        echo "Permissions on /etc/issue.net are already correct."
    fi
else
    echo "Error: /etc/issue.net not found or inaccessible."
fi

echo "Permission check complete."

