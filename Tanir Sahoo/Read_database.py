import sqlite3

conn = sqlite3.connect("shared_database.db")

c = conn.cursor()

query = "SELECT id FROM group_details ORDER BY id DESC;"

c.execute(query)

data = c.fetchall()
jt = data[0]
print(jt[0])
#for row in data:
    #print(row[0])

conn.close()
