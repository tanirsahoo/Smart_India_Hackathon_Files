import subprocess

def block_ssh_for_user(username):
    sshd_config = '/etc/ssh/sshd_config'
    subprocess.run(['sudo', 'cp', sshd_config, f'{sshd_config}.backup'])
    
    # Remove the user from AllowUsers if present
    subprocess.run(['sudo', 'sed', '-i', f'/AllowUsers.*{username}/d', sshd_config])
    
    subprocess.run(['sudo', 'systemctl', 'restart', 'ssh'])
    print(f"SSH access blocked for user '{username}'")

def main():
    username = input("Enter the username to block SSH access: ")

    block_ssh_for_user(username)

if __name__ == "__main__":
    main()

