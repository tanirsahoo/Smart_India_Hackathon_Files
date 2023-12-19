#!/bin/bash

# This script performs system hardening tasks for Ubuntu Desktop

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

echo "Starting system hardening..."

# Ensure /dev/shm is configured
if ! grep -qs '/dev/shm' /etc/fstab; then
    echo "Configuring /dev/shm..."
    
    # Add configuration to /etc/fstab
    echo 'tmpfs /dev/shm tmpfs defaults 0 0' | sudo tee -a /etc/fstab > /dev/null

    # Remount /dev/shm
    sudo mount -o remount /dev/shm

    echo "Configuration complete."
else
    echo "/dev/shm is already configured."
fi

# Set secure permissions on sensitive files
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 644 /etc/group
chmod 600 /etc/gshadow

# Disable unnecessary services
echo "Disabling unnecessary services..."
systemctl disable avahi-daemon
systemctl disable cups

# Remove unnecessary packages
echo "Removing unnecessary packages..."
apt-get purge -y whoopsie popularity-contest

# Enable the Uncomplicated Firewall (UFW) and configure default rules
echo "Configuring firewall..."
ufw --force enable
ufw default deny incoming
ufw default allow outgoing

# Disable root login and password authentication
echo "Disabling root login and password authentication..."
sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
service ssh restart

# Enable automatic security updates
echo "Enabling automatic security updates..."
apt-get install -y unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades

echo "System hardening complete."

# Optional: Reboot the system
read -p "Do you want to reboot the system now? (y/n): " choice
if [ "$choice" == "y" ]; then
    echo "Rebooting..."
    reboot
else
    echo "Please reboot the system for changes to take effect."
fi

