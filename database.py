import sqlite3

conn = sqlite3.connect(
    "database.db",
    timeout=20
)

try:

    conn = sqlite3.connect(
        "database.db",
        timeout=20
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history
        (
        user_email,
        text_data,
        prediction
        )
        VALUES
        (
        ?,
        ?,
        ?
        )
        """,
        (
            session["user"],
            text,
            result
        )
    )

    conn.commit()

finally:

    conn.close()


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT UNIQUE,
password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_email TEXT,
text_data TEXT,
prediction TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created")