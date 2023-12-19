import subprocess
import sqlite3

def remove_user_from_group(username, group_name):
    try:
        subprocess.run(['sudo', 'gpasswd', '-d', username, group_name], check=True)
        database_read(group_name , username)
        print(f"User '{username}' removed from group '{group_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing user from group: {e}")

def database_read(group_name , username):
   conn = sqlite3.connect("shared_database.db")
   c = conn.cursor()
   query = f"SELECT users FROM group_details WHERE name='{group_name}';"
   c.execute(query)
   data = c.fetchall()
   yom = data[0]
   dta = yom[0]
   print(type(dta))
   print(dta)
   itm_array = dta.split(',')
   itm_array.remove(username)
   result_string = ', '.join(itm_array)
   query = f"UPDATE group_details SET users = {result_string} WHERE name = {username};"
   c.execute(query)
   #return data
   conn.close()

def main():
    username = input("Enter the username: ")
    group_name = input("Enter the group name: ")

    remove_user_from_group(username, group_name)

if __name__ == "__main__":
    main()
