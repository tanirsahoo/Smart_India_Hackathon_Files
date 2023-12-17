#!/bin/bash

LOG_FILE="/var/log/failed_login_attempts.log"
AUTH_LOG="/var/log/auth.log"

# Function to log failed login attempts
log_failed_attempts() {
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    local hostname=$(hostname)
    local user="$1"

    echo "$timestamp - $hostname - Failed login attempt for user: $user" >> "$LOG_FILE"
}

# Monitor the authentication log for failed login attempts
tail -n0 -F "$AUTH_LOG" | while read line; do
    if [[ "$line" == *"sshd"* && "$line" == *"Failed password"* ]]; then
        # Extract the username from the log entry
        user=$(echo "$line" | awk '{print $11}')
        log_failed_attempts "$user"
    fi
done
