import grp
import sqlite3

#def list_all_groups():
    #try:
        #groups = grp.getgrall()
        #print("All groups on the system:")
        #for group in groups:
            #print(group.gr_name)
    #except Exception as e:
        #print(f"Error listing groups: {e}")

def database_read():
   conn = sqlite3.connect("shared_database.db")
   c = conn.cursor()
   query = "SELECT name FROM group_details;"
   try:
       c.execute(query)
       data = c.fetchall()
       return data
       conn.close()
   except sqlite3.Error as e:
       print("There is some problem in displaying the groups created. The exception is: " , e)

def main():
    list_itm = database_read()
    print(list_itm)

if __name__ == "__main__":
    main()
