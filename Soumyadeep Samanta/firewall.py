import subprocess

def enable_firewall():
    try:
        # Enable the UFW firewall
        subprocess.run(['sudo', 'ufw', 'enable'], check=True)
        print("Firewall enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def disable_firewall():
    try:
        # Disable the UFW firewall
        subprocess.run(['sudo', 'ufw', 'disable'], check=True)
        print("Firewall disabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def allow_ports(ports):
    try:
        # Allow specified ports through the firewall
        for port in ports:
            subprocess.run(['sudo', 'ufw', 'allow', str(port)], check=True)
        print("Ports allowed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Enable Firewall")
        print("2. Disable Firewall")
        print("3. Allow Custom Ports")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            enable_firewall()
        elif choice == '2':
            disable_firewall()
        elif choice == '3':
            ports_str = input("Enter custom ports separated by commas (e.g., 80,443): ")
            ports = [int(p.strip()) for p in ports_str.split(',')]
            allow_ports(ports)
        elif choice == '4':
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
