import pkg_resources
import subprocess

# Name of the package to check for
package_name = "multipledispatch"

def is_package_installed(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def install_package(package_name):
    try:
        subprocess.check_call(["pip3", "install", package_name])
        print(f"{package_name} has been successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

if __name__ == "__main__":
    if is_package_installed(package_name):
        print(f"{package_name} is already installed.")
    else:
        print(f"{package_name} is not installed. Installing...")
        install_package(package_name)

