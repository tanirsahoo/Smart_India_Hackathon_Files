#!/bin/bash

# Check if nfs-kernel-server package is installed
if command -v nfsd &> /dev/null; then
    echo "Uninstalling NFS server..."
    sudo apt-get purge nfs-kernel-server
    sudo apt-get autoremove
    echo "NFS server has been uninstalled."
else
    echo "NFS server is not installed."
fi

# Check if nfs-common package is installed
if command -v mount.nfs &> /dev/null; then
    echo "Uninstalling NFS client..."
    sudo apt-get purge nfs-common
    sudo apt-get autoremove
    echo "NFS client has been uninstalled."
else
    echo "NFS client is not installed."
fi
