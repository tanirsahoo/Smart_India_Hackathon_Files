import grp
import subprocess
import sqlite3

def create_group(group_name):
    try:
        subprocess.run(['sudo', 'addgroup', group_name], check=True)
        print(f"Group '{group_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating group: {e}")
        
def database_read():
   conn = sqlite3.connect("shared_database.db")
   c = conn.cursor()
   query = "SELECT id FROM group_details ORDER BY id DESC;"
   c.execute(query)
   data = c.fetchall()
   #print("===============")
   #print(data)
   #print("===============")
   if(len(data) == 0):
      return "0"
   else:
      jt = data[0]
      return jt[0]
   conn.close()

def database_create(group_name , user_list):
   database_name = "shared_database.db"
   table_name = "group_details"
   connection = sqlite3.connect(database_name)
   cursor = connection.cursor()
   cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS group_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    users TEXT
    )
    """)
   id = int(database_read())
   id = (id + 1)
   id = str(id)
   #print(type(id))
   #print(id)
   data = [
       (group_name, user_list),
   ]
   insert_sql = f"""
   INSERT INTO `group_details` (`name`, `users`) VALUES ({group_name}, {user_list});
   """
   try:
       cursor.executemany(insert_sql, data)
   except sqlite3.Error as e:
       print("The error is: ", e)
   finally: 
       connection.commit()
       connection.close()

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
    group_name = group_name.lower()
    #create_group(group_name)

    user_list = input("Enter a comma-separated list of users to add to the group: ")
    print(type(user_list))
    users = [user.strip() for user in user_list.split(',')]
    #print(users)
    database_create(group_name , user_list)
    #add_users_to_group(group_name, users)
    #get_group_members(group_name)

if __name__ == "__main__":
    main()
