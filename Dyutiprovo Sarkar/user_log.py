import subprocess

def get_user_login_info():
    try:
        # Run the 'last' command to get user login information
        result = subprocess.run(['last'], capture_output=True, text=True, check=True)

        # Print the result (user login information)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the command execution
        print(f"Error: {e}")

if __name__ == "__main__":
    get_user_login_info()
