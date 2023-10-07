import subprocess
import getpass

def create_group(id, name):
    try:
        print("Enter the admin password")
        password = getpass.getpass()
        subprocess.run(input=password.encode(), check=True)
        print(f"Group '{name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating group '{name}': {e}")

def add_user_to_group(username):
    try:
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user '{username}': {e}")

def check_which_group(username):
    try:
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user '{username}': {e}")

def check_group_users(username):
    try:
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user '{username}': {e}")

def delete_group(username):
    try:
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user '{username}': {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create Group")
        print("2. Add User to a Group")
        print("3. Groups a User is a part of")
        print("4. Users of a Group")
        print("5. Delete Group")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id=input("Enter group id(>5000) : ")
            name = input("Enter group name : ")
            create_group(id,name)
        elif choice == "2":
            add_user_to_group
        elif choice == "3":
            check_which_group
        elif choice == "4":
            check_group_users
        elif choice == "5":
            delete_group
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

