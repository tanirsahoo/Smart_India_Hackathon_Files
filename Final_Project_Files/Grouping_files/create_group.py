import grp
import subprocess

def create_group(group_name):
    try:
        subprocess.run(['sudo', 'addgroup', group_name], check=True)
        print(f"Group '{group_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating group: {e}")

def add_users_to_group(group_name, users):
    try:
        for user in users:
            subprocess.run(['sudo', 'adduser', user, group_name], check=True)
            print(f"User '{user}' added to group '{group_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding users to group: {e}")

def get_group_members(group_name):
    try:
        group_info = grp.getgrnam(group_name)
        members = group_info.gr_mem
        print(f"Members of group '{group_name}': {', '.join(members)}")
    except KeyError:
        print(f"Group '{group_name}' not found.")

def main():
    group_name = input("Enter the name of the group: ")
    create_group(group_name)

    user_list = input("Enter a comma-separated list of users to add to the group: ")
    users = [user.strip() for user in user_list.split(',')]

    add_users_to_group(group_name, users)
    get_group_members(group_name)

if __name__ == "__main__":
    main()
