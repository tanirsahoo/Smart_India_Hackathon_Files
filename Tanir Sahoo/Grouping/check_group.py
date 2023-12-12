import subprocess

def get_user_groups(username):
    try:
        result = subprocess.run(['groups', username], capture_output=True, text=True, check=True)
        groups = result.stdout.strip().split(":")[1].strip().split()
        print(f"Groups for user '{username}': {', '.join(groups)}")
    except subprocess.CalledProcessError as e:
        print(f"Error getting groups for user: {e}")

def main():
    username = input("Enter the username: ")
    get_user_groups(username)

if __name__ == "__main__":
    main()
