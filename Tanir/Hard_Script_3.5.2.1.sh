#!/bin/bash

# Check if nft command is available
if ! command -v nft &> /dev/null; then
    echo "Installing nftables..."
    sudo apt-get update
    sudo apt-get install -y nftables
    echo "nftables has been installed."
else
    echo "nftables is already installed."
fi
