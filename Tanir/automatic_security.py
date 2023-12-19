import subprocess
import sqlite3
from datetime import datetime

def update_system():
  """
  This function updates the Ubuntu system, including security updates.
  """
  subprocess.run("sudo apt update", shell=True, check=True)
  subprocess.run("sudo apt upgrade -y", shell=True, check=True)
  subprocess.run("sudo apt install unattended-upgrades", shell=True, check=True)
  #subprocess.run("sudo unattended-upgrades --enable-automatic-kernel-upgrade", shell=True, check=True)
  return 1

def database_update(time_give):
  DB_FILE = "autoupdate_database.db"
  connection = sqlite3.connect(DB_FILE)
  cursor = connection.cursor()
  create_table_sql = """
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   days VARCHAR(255) NOT NULL
   );
   """
  cursor.execute(create_table_sql)
  data = [
   (f'{time_give}'),
  ]
  insert_data_sql = f"INSERT INTO users (days) VALUES ({time_give});"
  cursor.execute(insert_data_sql)
  connection.commit()
  connection.close()
  
def check_time():
   conn = sqlite3.connect("autoupdate_database.db")
   c = conn.cursor()
   query = "SELECT days FROM users ORDER BY id DESC;"
   c.execute(query)
   data = c.fetchall()
   jt = data[0]
   return jt[0]
   conn.close()

def run_function():
  #check_time()
  epoch = datetime(1970, 1, 1)
  current_time = datetime.now()
  total_days = (current_time - epoch).days
  check_days = int(check_time())
  if((total_days - check_days) > 90):
     return 1
  else:
     return 0
     
def main():
  """
  This function calls the update_system function.
  """
  if(run_function() == 1):
  #try:
    check_d = update_system()
    print(check_d)
    if(check_d == 1):
       epoch = datetime(1970, 1, 1)
       current_time = datetime.now()
       total_days = (current_time - epoch).days
       total_days = str(total_days)
       database_update(total_days)
    else:
       print("Error in making updates.")
  else:
    print("System is up to date")   
    
if __name__ == "__main__":
  main()
