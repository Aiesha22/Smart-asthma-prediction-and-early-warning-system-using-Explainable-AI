import sqlite3
import pandas as pd

DATABASE = "asthma.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        bmi REAL,
        prediction TEXT,
        probability REAL,
        final_risk REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def create_users_table():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT UNIQUE,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'Patient'
    )
    """)

    conn.commit()
    conn.close()   


def save_prediction(age, bmi, prediction, probability, final_risk):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history
    (age, bmi, prediction, probability, final_risk)
    VALUES (?, ?, ?, ?, ?)
    """, (age, bmi, prediction, probability, final_risk))

    conn.commit()
    conn.close()


def load_history():
    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM history ORDER BY id DESC",
        conn
    )

    conn.close()
    return df

def delete_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")

    conn.commit()

    conn.close()

def create_users_table():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'Doctor'
    )
    """)

    conn.commit()
    conn.close()    