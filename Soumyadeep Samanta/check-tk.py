import subprocess

# Check if python3-tk is already installed
try:
    subprocess.run(["python3", "-c", "import tkinter"], check=True)
    print("python3-tk is already installed.")
except subprocess.CalledProcessError:
    # If an error occurred, it means tkinter is not installed, so we'll try to install it
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
        print("python3-tk has been installed.")
    except subprocess.CalledProcessError:
        print("Failed to install python3-tk. Please check your internet connection or try manually.")

