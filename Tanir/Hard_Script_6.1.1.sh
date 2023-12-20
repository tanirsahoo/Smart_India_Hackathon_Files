#!/bin/bash

passwd_file="/etc/passwd"
correct_permissions="644"

# Check current permissions
current_permissions=$(stat -c "%a" $passwd_file)

if [ "$current_permissions" != "$correct_permissions" ]; then
    echo "Setting correct permissions on $passwd_file..."
    sudo chmod $correct_permissions $passwd_file
    echo "Permissions have been set to $correct_permissions."
else
    echo "Permissions on $passwd_file are already correct."
fi
