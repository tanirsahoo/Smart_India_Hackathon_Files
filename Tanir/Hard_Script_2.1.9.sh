
#!/bin/bash


if command -v apache2 &> /dev/null; then
    echo "Uninstalling Apache (HTTP server)..."
    sudo apt-get purge apache2
    sudo apt-get autoremove
    echo "Apache (HTTP server) has been uninstalled."
else
    echo "Apache (HTTP server) is not installed."
fi
