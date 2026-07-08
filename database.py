import sqlite3
from datetime import datetime, timedelta

def create_table():
    try:
        conn = sqlite3.connect("history2.db")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS product_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            name TEXT,
            price INTEGER,
            created_at TEXT,
            size TEXT,
            bulk_qty INTEGER,
            bulk_price INTEGER
        )""")
    conn.commit()
    conn.close()



def insert_values(code, name, price,  created_at, size=None, bulk_qty=None, bulk_price=None):
    try:
        conn = sqlite3.connect("history2.db")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))

    cursor = conn.cursor()
    cursor.execute("""INSERT INTO product_history(code, name, price, created_at, size, bulk_qty, bulk_price)
    VALUES(?, ?, ?, ?, ?, ?, ?) """, (code, name, price, created_at, size, bulk_qty, bulk_price))
    conn.commit()
    conn.close()



def view_history():
    try:
        conn = sqlite3.connect("history2.db")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))

    cursor = conn.cursor()
    cursor.execute("""SELECT code, name, price, size, bulk_qty, bulk_price FROM product_history ORDER BY id DESC""")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_history():
    cutoff = datetime.now() - timedelta(days =  7)
    deletion_date = cutoff.strftime("%Y-%m-%d %H:%M:%S")

    try:
        conn = sqlite3.connect("history2.db")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM product_history
    WHERE created_at < ?""", (deletion_date,))
    conn.close()
