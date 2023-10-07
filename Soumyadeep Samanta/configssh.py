#!/usr/bin/env python3
import os

# Define the custom SSH configuration file path
custom_ssh_config_file = '/etc/ssh/admin_sshd_config'

# Define the administrators who can block SSH access
admin_usernames = ['soumyadeep_samanta', 'dyuti']

def create_custom_ssh_config():
    # Create or overwrite the custom SSH configuration file
    with open(custom_ssh_config_file, 'w') as config_file:
        config_file.write("# Custom SSH Configuration for Administrators\n")
        config_file.write("# Only administrators can block SSH access\n")
        for username in admin_usernames:
            config_file.write(f"AllowUsers {username}\n")
        config_file.write("PasswordAuthentication yes\n")

def reload_ssh_service():
    # Reload the SSH service to apply the changes
    os.system('systemctl reload ssh')

def main():
    # Check if the script is run as root
    if os.geteuid() != 0:
        print("This script must be run as root.")
        exit(1)

    try:
        # Create the custom SSH configuration
        create_custom_ssh_config()

        # Reload the SSH service
        reload_ssh_service()

        print("SSH access configuration for administrators has been updated.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
