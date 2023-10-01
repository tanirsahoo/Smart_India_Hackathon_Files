import subprocess

def check_firewall_status():
    try:
        # Check if UFW (Uncomplicated Firewall) is installed
        subprocess.check_call(['ufw', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("UFW is not installed. Installing it...")
        subprocess.call(['sudo', 'apt', 'update'])
        subprocess.call(['sudo', 'apt', 'install', 'ufw', '-y'])

    # Check UFW status
    status = subprocess.check_output(['sudo', 'ufw', 'status'], text=True)
    return "Status: active" in status
    
def enable_ufw():
    try:
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        print("UFW enabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling UFW: {e}")
        return

def check_ssh_status():
    try:
        # Check if SSH server is installed
        subprocess.check_call(['dpkg', '-l', 'openssh-server'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False
        
def allow_ssh():
    try:
        subprocess.run(["sudo", "ufw", "allow", "OpenSSH"], check=True)
        print("SSH access allowed.")
    except subprocess.CalledProcessError as e:
        print(f"Error allowing SSH: {e}")
        return

def is_port_open(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Set a timeout for the connection attempt
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def allow_custom_ports(ports):
    for port in ports:
        try:
            subprocess.run(["sudo", "ufw", "allow", str(port)], check=True)
            print(f"Port {port} allowed.")
        except subprocess.CalledProcessError as e:
            print(f"Error allowing port {port}: {e}")

def main():
    # Enable UFW
    firewall_enabled = check_firewall_status()

    if not firewall_enabled:
        enable_ufw()

    # Allow SSH
    ssh_enabled = check_ssh_status()

    if not ssh_enabled:
        allow_ssh()

    # Define additional ports to allow (e.g., 80 for HTTP, 443 for HTTPS)
    host = "localhost"
    custom_ports = [80, 443]

    # Allow custom ports
    if is_port_open(host, custom_ports):
        allow_custom_ports(custom_ports)

if __name__ == "__main__":
    main()

