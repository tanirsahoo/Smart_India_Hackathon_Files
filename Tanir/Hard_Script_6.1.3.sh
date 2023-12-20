#!/bin/bash

group_file="/etc/group"
correct_permissions="644"

# Check current permissions
current_permissions=$(stat -c "%a" "$group_file" 2>/dev/null)

if [ "$current_permissions" != "$correct_permissions" ]; then
    echo "Setting correct permissions on $group_file..."
    sudo chmod "$correct_permissions" "$group_file"
    echo "Permissions have been set to $correct_permissions."
else
    echo "Permissions on $group_file are already correct."
fi
