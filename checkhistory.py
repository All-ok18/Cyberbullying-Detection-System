import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM history")

rows = cursor.fetchall()

print("Total Records:", len(rows))

for row in rows:
    print(row)

conn.close()