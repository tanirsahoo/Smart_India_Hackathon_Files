#!/bin/bash

# This script checks whether all AppArmor profiles are in enforce or complain mode

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Checking AppArmor profile modes..."

# Check if aa-status command is available
if command -v aa-status > /dev/null; then
    # Get AppArmor status
    apparmor_status=$(aa-status --quiet)

    # Check if any profiles are in complain mode
    if echo "$apparmor_status" | grep -q "profiles in complain mode"; then
        echo "AppArmor has profiles in complain mode:"
        echo "$apparmor_status"
    else
        echo "All AppArmor profiles are in enforce mode."
    fi
else
    echo "AppArmor is not installed on this system."
fi

echo "Check complete."

