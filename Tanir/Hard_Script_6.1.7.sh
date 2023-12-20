#!/bin/bash

gshadow_file="/etc/gshadow"
correct_permissions="640"

# Check current permissions
current_permissions=$(stat -c "%a" "$gshadow_file" 2>/dev/null)

if [ "$current_permissions" != "$correct_permissions" ]; then
    echo "Setting correct permissions on $gshadow_file..."
    sudo chmod "$correct_permissions" "$gshadow_file"
    echo "Permissions have been set to $correct_permissions."
else
    echo "Permissions on $gshadow_file are already correct."
fi
