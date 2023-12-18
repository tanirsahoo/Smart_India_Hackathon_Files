import subprocess
import sqlite3

def delete_group(group_name):
    try:
        #subprocess.run(['sudo', 'delgroup', group_name], check=True)
        database_read(group_name)
        #print(f"Group '{group_name}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting group as it doesn't exist: {e}")

def database_read(group_name):
   conn = sqlite3.connect("shared_database.db")
   c = conn.cursor()
   #query = f"DELETE FROM group_details WHERE name = '{group_name}';"
   sql = "DELETE FROM group_details WHERE name = ?"

    # Value to delete (in this case, "Kaizen")
   entry_to_delete = (f"{group_name}",)

    # Execute the DELETE SQL statement
    #c.execute(sql, entry_to_delete)

    # Commit the changes to the database
    #conn.commit()
   #print(query)
   try:
       c.execute(sql, entry_to_delete)
       conn.commit()
       #c.execute(query)
   except sqlite3.Error as e:
       print("Cannot delete the Group from database, but it might be present in the system. Error: " , e)
      

def main():
    group_name = input("Enter the name of the group to delete: ")
    #group_name = group_name.lower()
    delete_group(group_name)

if __name__ == "__main__":
    main()
