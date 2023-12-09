import os
import subprocess

def generate_gpg_password():
    # Generate a random password using GPG
    command = "gpg --gen-random --armor 1 16"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0:
        return output.decode().strip()
    else:
        print("Error generating GPG password:", error.decode().strip())
        return None

def delete_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

def encrypt_file_with_password(file_path, password):
    # Encrypt the file using GPG symmetric encryption
    command = f"gpg --symmetric --passphrase {password} --output {file_path}.gpg {file_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        print(f"File '{file_path}' encrypted successfully.")
    else:
        print("Error encrypting the file:", error.decode().strip())

if __name__ == "__main__":
    # Generate a GPG password
    password = generate_gpg_password()

    if password:
        # Specify the file to be encrypted


        file_path = input("Enter file name : ").strip()

        # Encrypt the file using the generated password
        encrypt_file_with_password(file_path, password)
        delete_file(file_path)

    

