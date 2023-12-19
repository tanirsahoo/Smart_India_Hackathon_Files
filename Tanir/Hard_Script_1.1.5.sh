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

# Add noexec option if not present
if [[ ! "$current_opts" =~ "noexec" ]]; then
  sed -i '/\/tmp/s/\(defaults\)/\1,noexec/' /etc/fstab
  mount -o remount /tmp
  echo "noexec option set on /tmp partition"
else
  echo "noexec option is already set on /tmp partition"
fi

