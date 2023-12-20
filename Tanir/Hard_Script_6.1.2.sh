#!/bin/bash

passwd_backup_file="/etc/passwd-"
correct_permissions="600"

# Check current permissions
current_permissions=$(stat -c "%a" "$passwd_backup_file" 2>/dev/null)

if [ "$current_permissions" != "$correct_permissions" ]; then
    echo "Setting correct permissions on $passwd_backup_file..."
    sudo chmod "$correct_permissions" "$passwd_backup_file"
    echo "Permissions have been set to $correct_permissions."
else
    echo "Permissions on $passwd_backup_file are already correct."
fi
