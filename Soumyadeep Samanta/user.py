import subprocess

def create_user(username, password):
    try:
        subprocess.run(["sudo", "useradd", "-m", username], check=True)
        subprocess.run(["sudo", "passwd", username], input=password.encode(), check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user '{username}': {e}")

def delete_user(username):
    try:
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user '{username}': {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Delete User")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter the username to create: ")
            password = input(f"Enter the password for user '{username}': ")
            create_user(username, password)
        elif choice == "2":
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

