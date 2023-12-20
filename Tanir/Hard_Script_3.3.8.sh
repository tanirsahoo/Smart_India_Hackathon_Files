#!/bin/bash

# Check if TCP SYN Cookies are enabled
syn_cookies_enabled=$(sysctl -n net.ipv4.tcp_syncookies)

if [ "$syn_cookies_enabled" -eq 0 ]; then
    echo "Enabling TCP SYN Cookies..."
    sudo sysctl -w net.ipv4.tcp_syncookies=1
    echo "TCP SYN Cookies have been enabled."
else
    echo "TCP SYN Cookies are already enabled."
fi
