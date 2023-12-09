import subprocess
import sqlite3

def get_users_created_by_root():
    try:
        # Use the 'ls' command to list users created by root in the /home directory
        process = subprocess.Popen(['ls', '/home'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        usernames = output.decode('utf-8').split()
        return usernames
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    usernames = get_users_created_by_root()
    if usernames:
        #print("Usernames created by root:")
        #for username in usernames:
        #********************Variable usernames is an array containing the names of the directories present inside the /home folder****************
        print(usernames)
    else:
        print()
