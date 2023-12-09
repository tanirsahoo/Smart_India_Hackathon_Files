import subprocess
import getpass, os

def decrypt_file_with_password(file_path, password):
    # Decrypt the file using GPG symmetric decryption
    command = f"gpg --decrypt --passphrase {password} --output {file_path[:-4]} {file_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        print(f"File '{file_path}' decrypted successfully.")
    else:
        print("Error decrypting the file:", error.decode().strip())

def delete_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

if __name__ == "__main__":
    # Specify the encrypted file to be decrypted
    encrypted_file_path = input("Enter file name : ").strip()

    # Get the GPG password from the user
    password = getpass.getpass("Enter the GPG password: ")

    # Decrypt the file using the provided password
    decrypt_file_with_password(encrypted_file_path, password)
    delete_file(encrypted_file_path)
