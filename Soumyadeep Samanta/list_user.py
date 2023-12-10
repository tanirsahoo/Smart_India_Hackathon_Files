import subprocess

def get_sudo_created_users():
    result = subprocess.run(['getent', 'passwd'], stdout=subprocess.PIPE, text=True)
    user_lines = result.stdout.splitlines()

    sudo_created_users = []

    for user_line in user_lines:
        # Extract user information from the passwd file
        user_info = user_line.split(':')
        username = user_info[0]
        uid = user_info[2]

        # Check if the user was created by a sudo user
        if uid != '0' and int(uid) >= 1000:
            sudo_created_users.append(username)

    return sudo_created_users

def get_admin_users(usernames):
    admin_users = []

    for username in usernames:
        # Check if the user is a member of the sudo group
        try:
            subprocess.run(['getent', 'group', 'sudo'], check=True, stdout=subprocess.PIPE)
            result = subprocess.run(['id', '-nG', username], check=True, stdout=subprocess.PIPE, text=True)
            
            # Check if the user is a member of the sudo group
            if 'sudo' in result.stdout.split():
                admin_users.append(username)
        except subprocess.CalledProcessError:
            pass

    return admin_users

def main():
    sudo_created_users = get_sudo_created_users()

    print("Users Created by Sudo User:")
    for username in sudo_created_users:
        print(f" - {username}")

    admin_users = get_admin_users(sudo_created_users)

    print("\nUsers with Administrator Settings:")
    for username in admin_users:
        print(f" - {username}")

if __name__ == "__main__":
    main()
