#!/bin/bash

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root"
  exit 1
fi

# Backup the /etc/fstab file
cp /etc/fstab /etc/fstab.bak

# Get the current mount options for /tmp
current_opts=$(grep "/tmp" /etc/fstab | awk '{print $4}')

# Add nosuid option if not present
if [[ ! "$current_opts" =~ "nosuid" ]]; then
  sed -i '/\/tmp/s/\(defaults\)/\1,nosuid/' /etc/fstab
  mount -o remount /tmp
  echo "nosuid option set on /tmp partition"
else
  echo "nosuid option is already set on /tmp partition"
fi

