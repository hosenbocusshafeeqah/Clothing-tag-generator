import sqlite3
from datetime import datetime, timedelta

def create_table():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS product_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            name TEXT,
            price REAL,
            created_at TEXT,
            size TEXT
        )""")
    conn.commit()
    conn.close()



def insert_values(code, name, price,  created_at, size = None):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO product_history(code, name, price, created_at, size)
    VALUES(?, ?, ?, ?, ?) """, (code, name, price, created_at, size))
    conn.commit()
    conn.close()



def view_history():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT code, name, price, size FROM product_history""")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_history():
    cutoff = datetime.now() - timedelta(days =  7)
    deletion_date = cutoff.strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM product_history
    WHERE created_at < ?""", (deletion_date,))
    rows = cursor.fetchall()
    conn.close()
