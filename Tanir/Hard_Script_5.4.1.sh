#!/bin/bash

# Check if the script is executed with sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or with sudo."
  exit 1
fi

# Backup the original PAM configuration file
cp /etc/security/opasswd /etc/security/opasswd.bak

# Set the number of previous passwords to remember (adjust as needed)
password_history_count=5

# Modify the PAM configuration to limit password reuse
echo "password required pam_pwhistory.so remember=${password_history_count}" >> /etc/pam.d/common-password

echo "Password reuse is now limited to the last ${password_history_count} passwords."

exit 0
