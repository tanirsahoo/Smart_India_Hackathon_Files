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

def save_users_to_sql(usernames, db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        # Create a table to store usernames
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS root_created_users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE
            )
        ''')

        # Insert usernames into the table
        for username in usernames:
            cursor.execute("INSERT OR IGNORE INTO root_created_users (username) VALUES (?)", (username,))

        conn.commit()
        print(f"Usernames created by root saved to {db_filename}")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get the list of users created by root
    usernames = get_users_created_by_root()

    # Print the usernames in the terminal
    if usernames:
        print("Usernames created by root:")
        for username in usernames:
            print(username)
    else:
        print("No users created by root found in the /home directory.")

    # Save the usernames to an SQLite database
    save_users_to_sql(usernames, "root_created_users.db")

