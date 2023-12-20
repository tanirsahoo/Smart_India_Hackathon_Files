#!/bin/bash

# This script performs system hardening tasks for Ubuntu Desktop, including regular filesystem checks

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Starting system hardening..."

# Install required packages (if not already installed)
apt-get update
apt-get install -y --no-install-recommends cron

# Configure daily filesystem checks
echo "Configuring daily filesystem checks..."

# Add a cron job to schedule fsck at a convenient time (e.g., during system startup)
echo "@reboot root /sbin/fsck -a -C -T -t ext4 /dev/sda1" > /etc/cron.d/fsck

echo "Filesystem checks are scheduled."

echo "System hardening complete."

# Optional: Reboot the system
read -p "Do you want to reboot the system now? (y/n): " choice
if [ "$choice" == "y" ]; then
    echo "Rebooting..."
    reboot
else
    echo "Please reboot the system for changes to take effect."
fi

