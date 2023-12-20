#!/bin/bash

# Ensure root is the only UID 0 account
root_users=$(awk -F: '$3 == 0 {print $1}' /etc/passwd)

if [ "$(echo "$root_users" | wc -w)" -eq 1 ]; then
    echo "Only root has UID 0. No action needed."
else
    echo "Fixing UID 0 accounts..."
    sudo usermod -u 1 -o -g 1 -G 1 -d /root -s /bin/bash -c "Default root user" -m -l root root
    echo "UID 0 accounts have been fixed."
fi
