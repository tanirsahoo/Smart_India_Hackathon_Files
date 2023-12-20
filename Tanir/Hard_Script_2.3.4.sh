#!/bin/bash


if command -v telnet &> /dev/null; then
    echo "Uninstalling Telnet client..."
    sudo apt-get purge telnet
    sudo apt-get autoremove
    echo "Telnet client has been uninstalled."
else
    echo "Telnet client is not installed."
fi
