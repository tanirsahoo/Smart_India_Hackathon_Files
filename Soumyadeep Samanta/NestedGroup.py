import subprocess

def create_group(group_name):
    subprocess.run(['sudo', 'addgroup', group_name])

def add_users_to_group(usernames, group_name):
    for username in usernames:
        subprocess.run(['sudo', 'usermod', '-aG', group_name, username])
        print(f"User '{username}' added to group '{group_name}'")

def add_group_to_group(child_group, parent_group):
    subprocess.run(['sudo', 'gpasswd', '-a', f'@{child_group}', parent_group])
    print(f"Group '{child_group}' added to group '{parent_group}'")

def main():
    parent_group_name = input("Enter the parent group name: ")
    create_group(parent_group_name)

    child_group_name = input("Enter the child group name: ")
    create_group(child_group_name)
    add_group_to_group(child_group_name, parent_group_name)

    user_count = int(input("Enter the number of users to add to the child group: "))
    usernames = [input(f"Enter username {i + 1}: ") for i in range(user_count)]

    add_users_to_group(usernames, child_group_name)

if __name__ == "__main__":
    main()

