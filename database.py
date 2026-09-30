import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path(__file__).resolve().parent / "students.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL,
            attendance REAL NOT NULL,
            mathematics REAL NOT NULL,
            dbms REAL NOT NULL,
            python REAL NOT NULL,
            machine_learning REAL NOT NULL,
            average_marks REAL NOT NULL
        )
        """)
        con.commit()

def add_student(name, roll_no, department, attendance, mathematics, dbms, python, machine_learning, average_marks):
    with get_connection() as con:
        con.execute("""
        INSERT INTO students
        (name, roll_no, department, attendance, mathematics, dbms, python, machine_learning, average_marks)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, roll_no, department, attendance, mathematics, dbms, python, machine_learning, average_marks))
        con.commit()

def get_students():
    with get_connection() as con:
        return pd.read_sql_query("SELECT * FROM students ORDER BY id DESC", con)

def delete_student(roll_no):
    with get_connection() as con:
        con.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
        con.commit()
