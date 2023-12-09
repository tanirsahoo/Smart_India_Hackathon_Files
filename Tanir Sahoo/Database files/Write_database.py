import sqlite3

database_name = "my_database.db"
table_name = "users"
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
email TEXT NOT NULL UNIQUE
);
""")

data = [
    ["John Doe", "johndoe@example.com"],
    ["Jane Doe", "janedoe@example.com"],
]
insert_sql = f"""
INSERT INTO {table_name} (name, email)
VALUES (?, ?)
"""
cursor.executemany(insert_sql, data)
connection.commit()
connection.close()
