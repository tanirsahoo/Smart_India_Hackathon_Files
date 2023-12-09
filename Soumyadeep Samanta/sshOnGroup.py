import subprocess

def create_group(group_name):
    subprocess.run(['sudo', 'addgroup', group_name])

def check_group_exists(group_name):
    result = subprocess.run(['getent', 'group', group_name], stdout=subprocess.PIPE)
    return result.returncode == 0

def add_users_to_group(usernames, group_name):
    for username in usernames:
        subprocess.run(['sudo', 'usermod', '-aG', group_name, username])
        print(f"User '{username}' added to group '{group_name}'")

def enable_ssh_for_user(username):
    sshd_config = '/etc/ssh/sshd_config'
    subprocess.run(['sudo', 'cp', sshd_config, f'{sshd_config}.backup'])
    subprocess.run(['sudo', 'bash', '-c', f'echo "AllowUsers {username}" >> {sshd_config}'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'ssh'])
    print(f"SSH enabled for user '{username}'")

def main():
    group_name = input("Enter the group name: ")

    if not check_group_exists(group_name):
        create_group(group_name)
        print(f"Group '{group_name}' created.")

    user_count = int(input("Enter the number of existing users to add to the group: "))
    usernames = [input(f"Enter username {i + 1}: ") for i in range(user_count)]

    add_users_to_group(usernames, group_name)

    for username in usernames:
        enable_ssh_for_user(username)

if __name__ == "__main__":
    main()

