import subprocess

def is_ssh_enabled_for_user(username):
    sshd_config = '/etc/ssh/sshd_config'
    result = subprocess.run(['sudo', 'grep', f'^AllowUsers.*{username}', sshd_config], stdout=subprocess.PIPE)
    return result.returncode == 0

def main():
    username = input("Enter the username to check for SSH access: ")

    if is_ssh_enabled_for_user(username):
        print(f"SSH is enabled for user '{username}'.")
    else:
        print(f"SSH is not enabled for user '{username}'.")

if __name__ == "__main__":
    main()

