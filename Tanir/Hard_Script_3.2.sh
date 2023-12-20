#!/bin/bash

# Check if packet redirection is enabled
redirect_enabled=$(sysctl -n net.ipv4.conf.all.send_redirects)

if [ "$redirect_enabled" -eq 1 ]; then
    echo "Disabling packet redirection..."
    sudo sysctl -w net.ipv4.conf.all.send_redirects=0
    sudo sysctl -w net.ipv4.conf.default.send_redirects=0
    echo "Packet redirection has been disabled."
else
    echo "Packet redirection is already disabled."
fi

# Check if IP forwarding is enabled
forwarding_enabled=$(sysctl -n net.ipv4.ip_forward)

if [ "$forwarding_enabled" -eq 1 ]; then
    echo "Disabling IP forwarding..."
    sudo sysctl -w net.ipv4.ip_forward=0
    echo "IP forwarding has been disabled."
else
    echo "IP forwarding is already disabled."
fi