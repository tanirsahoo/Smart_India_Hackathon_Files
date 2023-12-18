import sqlite3

conn = sqlite3.connect("shared_database.db")

c = conn.cursor()

query = "SELECT * FROM group_details ORDER BY id DESC;"

c.execute(query)

data = c.fetchall()
print(data)
#for row in data:
    #print(row[0])

conn.close()
