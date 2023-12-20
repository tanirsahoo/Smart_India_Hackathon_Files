!/bin/bash

# This script ensures proper permissions on /etc/motd

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Checking permissions on /etc/motd..."

# Define the correct permissions for /etc/motd (e.g., read-only for all)
correct_permissions="644"

# Get current permissions on /etc/motd
current_permissions=$(stat -c "%a" /etc/motd 2>/dev/null)

if [[ -n "$current_permissions" ]]; then
    if [ "$current_permissions" != "$correct_permissions" ]; then
        echo "Updating permissions on /etc/motd..."
        
        # Set correct permissions
        chmod $correct_permissions /etc/motd

        echo "Permissions updated."
    else
        echo "Permissions on /etc/motd are already correct."
    fi
else
    echo "Error: /etc/motd not found or inaccessible."
fi

echo "Permission check complete."
