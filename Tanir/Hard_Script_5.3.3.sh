#!/bin/bash

sudo_log_file="/var/log/sudo.log"
alternative_sudo_log_file="/var/log/auth.log"

# Check if sudo log file exists
if [ -f "$sudo_log_file" ]; then
    echo "sudo log file exists: $sudo_log_file"
else
    # Check alternative location
    if [ -f "$alternative_sudo_log_file" ]; then
        echo "sudo log file exists at alternative location: $alternative_sudo_log_file"
    else
        echo "sudo log file does not exist. Creating..."
        sudo touch "$sudo_log_file"
        sudo chmod 640 "$sudo_log_file"
        echo "sudo log file created: $sudo_log_file"
    fi
fi
