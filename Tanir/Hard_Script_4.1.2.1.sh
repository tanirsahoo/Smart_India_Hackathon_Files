#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Auditd configuration file
auditd_config="/etc/audit/auditd.conf"

# Configuration parameter to check
config_parameter="max_log_file"

# Check if the configuration parameter exists in the auditd configuration file
if grep -q "^$config_parameter" "$auditd_config"; then
    echo "$config_parameter is configured in $auditd_config."
else
    echo "$config_parameter is not configured in $auditd_config."
fi

