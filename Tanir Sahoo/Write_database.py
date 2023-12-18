import sqlite3

database_name = "shared_database.db"
table_name = "group_details"
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
#cursor.execute(f"""
#CREATE TABLE IF NOT EXISTS {table_name} (
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#name TEXT NOT NULL UNIQUE,
#users TEXT NOT NULL UNIQUE
#);
#""")
group_name = "kaizenZ"
users = "tanir,harry,bibu"
data = [
   ["2", group_name, users],
]
insert_sql = f"""
INSERT INTO `group_details` (`id`, `name`, `users`) VALUES (?,?,?);
"""
cursor.executemany(insert_sql, data)
connection.commit()
connection.close()
