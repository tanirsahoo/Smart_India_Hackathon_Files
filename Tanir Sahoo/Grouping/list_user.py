import subprocess
import os
import pwd

def get_root_user():
    usr = get_sudo_created_users()
    for itm in usr:
    #username = os.getlogin()
    	user_info = pwd.getpwnam(itm)
    	uid = user_info.pw_uid
    	if(uid == 1000):
    	   return itm

#print(f"The UID of user '{username}' is: {uid}")

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
    root_user = get_root_user()
    print(root_user)
    
    sudo_created_users = get_sudo_created_users()
    del sudo_created_users[0]
    print(sudo_created_users)

    admin_users = get_admin_users(sudo_created_users)
    print(admin_users)


if __name__ == "__main__":
    main()
