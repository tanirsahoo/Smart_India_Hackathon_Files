#!/bin/bash

shadow_file="/etc/shadow"
correct_permissions="640"

# Check current permissions
current_permissions=$(stat -c "%a" "$shadow_file" 2>/dev/null)

if [ "$current_permissions" != "$correct_permissions" ]; then
    echo "Setting correct permissions on $shadow_file..."
    sudo chmod "$correct_permissions" "$shadow_file"
    echo "Permissions have been set to $correct_permissions."
else
    echo "Permissions on $shadow_file are already correct."
fi
