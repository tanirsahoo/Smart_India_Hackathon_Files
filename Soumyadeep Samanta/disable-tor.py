import subprocess

def disable_tor():
    try:
        # Stop the Tor service
        subprocess.run(['sudo', 'systemctl', 'stop', 'tor'])

        # Disable the Tor service from starting on boot
        subprocess.run(['sudo', 'systemctl', 'disable', 'tor'])

        print("Tor has been disabled.")
    except Exception as e:
        print(f"Error disabling Tor: {e}")

if __name__ == "__main__":
    disable_tor()

