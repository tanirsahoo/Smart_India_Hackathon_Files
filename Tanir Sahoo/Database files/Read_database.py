import sqlite3

conn = sqlite3.connect("my_database.db")

c = conn.cursor()

query = "SELECT * FROM users"

c.execute(query)

data = c.fetchall()

for row in data:
    print(row)

conn.close()
