import subprocess

def remove_user_from_group(username, group_name):
    try:
        subprocess.run(['sudo', 'gpasswd', '-d', username, group_name], check=True)
        print(f"User '{username}' removed from group '{group_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing user from group: {e}")

def main():
    username = input("Enter the username: ")
    group_name = input("Enter the group name: ")

    remove_user_from_group(username, group_name)

if __name__ == "__main__":
    main()
