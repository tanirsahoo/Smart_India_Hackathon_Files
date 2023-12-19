import subprocess

def block_port(port):
    # Delete previous iptables INPUT rules for the specified port
    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])

def enable_port(port):
    # Delete previous iptables INPUT rules for the specified port
    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])

def main():
    try:
        # Get user input for port number
        port = int(input("Enter the port number: "))
        # Get user choice
        choice = input("Enter 'block' to block the port or 'enable' to enable the port: ")

        if choice == 'block':
            block_port(port)
            print(f"Port {port} blocked successfully.")
        elif choice == 'enable':
            enable_port(port)
            print(f"Port {port} enabled successfully.")
        else:
            print("Invalid choice. Please enter 'block' or 'enable'.")

    except ValueError:
        print("Invalid port number. Please enter a valid integer.")

if __name__ == "__main__":
    main()
