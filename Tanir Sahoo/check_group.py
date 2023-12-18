import subprocess
import sqlite3

def get_user_groups(username):
    try:
        result = subprocess.run(['groups', username], capture_output=True, text=True, check=True)
        groups = result.stdout.strip().split(":")[1].strip().split()
        #print(groups)
        database_data = database_read()
        #print(database_data)
        ar=[]
        for item1 in database_data:
           for item2 in groups:
              if(item1[0].casefold() == item2.casefold()):
                 ar.append(item1[0])
        return ar
    except subprocess.CalledProcessError as e:
        print(f"Error getting groups for user: {e}")
        
def database_read():
   conn = sqlite3.connect("shared_database.db")
   c = conn.cursor()
   query = "SELECT name FROM group_details;"
   try:
       c.execute(query)
       data = c.fetchall()
       return data
   except sqlite3.Error as e:
       print("Wrong Case input or the username didn't match the database. The error is: ", e)
   conn.close()

def main():
    username = input("Enter the username: ")
    result = get_user_groups(username)
    print(result)

if __name__ == "__main__":
    main()
