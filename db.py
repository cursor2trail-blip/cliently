import sqlite3

def get_connection():
    return sqlite3.connect("test.db")

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    return cursor.fetchall()
