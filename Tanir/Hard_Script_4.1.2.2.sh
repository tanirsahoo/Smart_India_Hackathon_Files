#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Auditd configuration file
auditd_config="/etc/audit/auditd.conf"

# Configuration parameters to check
config_parameter="max_log_file_action"

# Expected value for max_log_file_action to retain logs
expected_value="keep_logs"

# Check if the configuration parameter exists in the auditd configuration file
if grep -q "^$config_parameter" "$auditd_config"; then
    current_value=$(grep "^$config_parameter" "$auditd_config" | awk '{print $3}')
    if [ "$current_value" == "$expected_value" ]; then
        echo "$config_parameter is configured to '$expected_value' in $auditd_config. Logs will be retained."
    else
        echo "$config_parameter is configured, but its value is not '$expected_value' in $auditd_config."
    fi
else
    echo "$config_parameter is not configured in $auditd_config."
fi

