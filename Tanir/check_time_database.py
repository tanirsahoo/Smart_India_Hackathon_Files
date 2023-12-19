import sqlite3

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
 ('0'),
]
insert_data_sql = f"INSERT INTO users (days) VALUES ('0');"
cursor.execute(insert_data_sql)
connection.commit()
connection.close()
