import socket
import requests
import subprocess
import shutil

def get_local_ip():
    try:
        # Create a socket object and connect to an external server (e.g., Google DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "Unable to get local IP address."

def get_public_ip():
    try:
        # Use a service like 'httpbin' to get the public IP address
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json()['origin']
        return public_ip
    except requests.RequestException:
        return "Unable to get public IP address."

def is_hydra_installed():
    return shutil.which("hydra") is not None

def install_hydra():
    subprocess.run(["sudo", "apt-get", "install", "hydra"])

def few():
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
import subprocess

def block_ssh(ip_address):
    # Block incoming SSH traffic from the specified IP address
    block_command = f"sudo iptables -A INPUT -p tcp --dport 22 -s {ip_address} -j DROP"

    try:
        subprocess.run(block_command, shell=True, check=True)
        print(f"SSH access blocked for {ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking SSH access for {ip_address}: {e}")

def unblock_ssh(ip_address):
    # Remove the rule blocking incoming SSH traffic from the specified IP address
    unblock_command = f"sudo iptables -D INPUT -p tcp --dport 22 -s {ip_address} -j DROP"

    try:
        subprocess.run(unblock_command, shell=True, check=True)
        print(f"SSH access unblocked for {ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error unblocking SSH access for {ip_address}: {e}")


    



    
    
    
if __name__ == "__main__":
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    print(f"Local IP Address: {local_ip}")
    print(f"Public IP Address: {public_ip}")
    few()
    target_ip = get_public_ip()  # Replace with the target IP address
    username_list = ["user1", "user2"]  # Replace with a list of existing usernames
    password_list = "/home/dyutiprovo/pass.txt"  # Replace with the path to a password list
    num_attempts_per_user = 5  # Adjust the number of attempts as needed

    generate_failed_login_attempts(target_ip, username_list, password_list, num_attempts_per_user)
    if num_attemps_per_user > 5:
    	block_ssh(target_ip)
    
    unblock_ssh(target_ip)
    
