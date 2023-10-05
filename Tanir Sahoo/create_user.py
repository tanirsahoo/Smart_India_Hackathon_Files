import getpass
import subprocess

def create_user(username, password):
  """Creates a new user with the specified username and password.

  Args:
    username: The username of the new user.
    password: The password of the new user.
  """

  # Create the new user.
  subprocess.run(["sudo", "useradd", username])

  # Set the password for the new user.
  subprocess.run(["sudo", "passwd", "-p", password, username])

if __name__ == "__main__":
  # Get the username and password from the admin.
  username = input("Enter the username of the new user: ")
  password = getpass.getpass("Enter the password for the new user: ")

  # Create the new user.
  create_user(username, password)

  # Print a success message.
  print(f"User {username} created successfully.")