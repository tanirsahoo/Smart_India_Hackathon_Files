import subprocess

def create_user():
    # Get user input for username and password
    username = input("Enter the new username: ")
    password = input("Enter the password for the new user: ")

    try:
        # Create a new user with the provided username
        subprocess.run(['sudo', 'useradd', '-m', username], check=True)

        # Set the user's password
        subprocess.run(['sudo', 'chpasswd'], input=f'{username}:{password}', text=True, check=True)

        print(f"User '{username}' created successfully with the provided password.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_user()
