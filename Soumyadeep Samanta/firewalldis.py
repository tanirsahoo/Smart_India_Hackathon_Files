import subprocess

def disable_firewall():
    try:
        # Disable the UFW (Uncomplicated Firewall)
        subprocess.run(["sudo", "ufw", "disable"], check=True)
        print("Firewall disabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to disable the firewall.")

if __name__ == "__main__":
    disable_firewall()

