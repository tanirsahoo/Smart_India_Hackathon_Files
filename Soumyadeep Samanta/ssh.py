import os

def main():
    # SSH configuration file
    sshd_config_path = '/etc/ssh/sshd_config'

    # Backup the original SSH configuration file
    backup_ssh_config(sshd_config_path)

    # Disable root login
    set_ssh_option(sshd_config_path, 'PermitRootLogin', 'no')

    # Allow only specific users to SSH
    allowed_users = ['user1', 'user2']  # Replace with your allowed users
    allow_users(sshd_config_path, allowed_users)

    # Set SSH protocol version to 2
    set_ssh_option(sshd_config_path, 'Protocol', '2')

    # Disable password-based authentication (use SSH keys instead)
    set_ssh_option(sshd_config_path, 'PasswordAuthentication', 'no')

    # Reload SSH service to apply changes
    reload_ssh_service()

def backup_ssh_config(config_path):
    backup_path = config_path + '.bak'
    if not os.path.exists(backup_path):
        os.system(f'sudo cp {config_path} {backup_path}')
        print(f'Backup created: {backup_path}')

def set_ssh_option(config_path, option, value):
    with open(config_path, 'r') as f:
        lines = f.readlines()

    with open(config_path, 'w') as f:
        for line in lines:
            if line.strip().startswith(option):
                f.write(f'{option} {value}\n')
            else:
                f.write(line)

    print(f'Setting {option} to {value}')

def allow_users(config_path, users):
    users_str = ' '.join(users)
    set_ssh_option(config_path, 'AllowUsers', users_str)

def reload_ssh_service():
    os.system('sudo systemctl reload ssh')
    print('SSH service reloaded')

if __name__ == "__main__":
    main()

