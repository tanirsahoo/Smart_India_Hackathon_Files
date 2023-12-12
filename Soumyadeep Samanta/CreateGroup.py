import subprocess

def create_group(group_name, num_users):
    # Create the group
    create_group_cmd = ['sudo', 'addgroup', group_name]
    subprocess.run(create_group_cmd, check=True)

    # Add users to the group
    for i in range(num_users):
        username = input(f"Enter username {i + 1}/{num_users}: ")
        add_user_to_group_cmd = ['sudo', 'adduser', username, group_name]
        subprocess.run(add_user_to_group_cmd, check=True)

if __name__ == "__main__":
    # Input the group name
    group_name = input("Enter the name of the group: ")

    # Input the number of users
    num_users = int(input("Enter the number of users to add: "))

    # Create the group and add users
    create_group(group_name, num_users)
    print(f"Group '{group_name}' created and {num_users} users added successfully.")

