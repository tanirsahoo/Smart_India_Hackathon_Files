#!/bin/bash

# Check if bind9 is installed
if command -v named &> /dev/null; then
    echo "Uninstalling BIND9 (DNS server)..."
    sudo apt-get purge bind9
    sudo apt-get autoremove
    echo "BIND9 (DNS server) has been uninstalled."
fi

# Check if systemd-resolved is installed
if command -v systemd-resolve &> /dev/null; then
    echo "Disabling systemd-resolved service..."
    sudo systemctl stop systemd-resolved
    sudo systemctl disable systemd-resolved
    sudo rm /etc/resolv.conf  # This removes the symlink to systemd-resolved's resolv.conf
    echo "systemd-resolved service has been disabled."
fi

# Check if other DNS-related packages are installed and uninstall them if necessary

# Add more checks and uninstallation steps as needed

echo "DNS-related packages have been checked and uninstalled if applicable."
