#!/bin/bash

LOG_FILE="/var/log/custom_log.log"

# Function to log information
log_info() {
    local message="$1"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - INFO: $message" >> "$LOG_FILE"
}

# Function to log errors
log_error() {
    local message="$1"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - ERROR: $message" >> "$LOG_FILE"
}

# Log system information
log_info "System information:"
log_info "Hostname: $(hostname)"
log_info "IP Address: $(hostname -I)"

# Add more log entries as needed

# Example: Log a custom event
log_info "Custom event: Something happened successfully!"



# Example: Log an error event
log_error "Error: Something went wrong!"

# Add more log entries as needed

# You can customize this script to include additional information or events specific to your environment.
