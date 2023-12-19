import subprocess

def install_bats():
    try:
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', 'bats'], check=True)
        print("bats installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing bats: {e}")

# Run the function to install bats
if __name__ == "__main__":
    install_bats()
