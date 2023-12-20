#!/bin/bash


# Check if ypbind (NIS client) is installed
if command -v ypbind &> /dev/null; then
    echo "Uninstalling NIS client..."
    sudo apt-get purge nis
    sudo apt-get autoremove
    echo "NIS client has been uninstalled."
else
    echo "NIS client is not installed."
fi
