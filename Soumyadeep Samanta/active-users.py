import subprocess

def get_active_users():
    try:
        # Run the 'who' command to get a list of currently logged-in users
        result = subprocess.run(['who'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            # Parse the output to extract usernames
            active_users = [line.split()[0] for line in result.stdout.splitlines()]
            return active_users
        else:
            print("Error running 'who' command:", result.stderr)
            return []
    except Exception as e:
        print("Error:", str(e))
        return []

def main():
    active_users = get_active_users()
    if active_users:
        print("Currently Active Users:")
        for user in active_users:
            print(user)
    else:
        print("No active users found.")

if __name__ == "__main__":
    main()

