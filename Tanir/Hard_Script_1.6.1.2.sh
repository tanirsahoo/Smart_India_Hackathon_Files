#!/bin/bash

# This script checks if AppArmor is enabled in the GRUB configuration

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Checking AppArmor status in GRUB..."

# Check if AppArmor is enabled in GRUB configuration
if grep -q "apparmor=1" /etc/default/grub; then
    echo "AppArmor is enabled in GRUB configuration."
else
    echo "AppArmor is not enabled in GRUB configuration."
fi

echo "Check complete."

