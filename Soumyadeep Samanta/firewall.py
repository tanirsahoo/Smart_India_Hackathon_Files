import subprocess

def enable_ufw():
    try:
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        print("UFW enabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling UFW: {e}")
        return

def allow_ssh():
    try:
        subprocess.run(["sudo", "ufw", "allow", "OpenSSH"], check=True)
        print("SSH access allowed.")
    except subprocess.CalledProcessError as e:
        print(f"Error allowing SSH: {e}")
        return

def allow_custom_ports(ports):
    for port in ports:
        try:
            subprocess.run(["sudo", "ufw", "allow", str(port)], check=True)
            print(f"Port {port} allowed.")
        except subprocess.CalledProcessError as e:
            print(f"Error allowing port {port}: {e}")

def main():
    # Enable UFW
    enable_ufw()

    # Allow SSH
    allow_ssh()

    # Define additional ports to allow (e.g., 80 for HTTP, 443 for HTTPS)
    custom_ports = [80, 443]

    # Allow custom ports
    allow_custom_ports(custom_ports)

if __name__ == "__main__":
    main()

