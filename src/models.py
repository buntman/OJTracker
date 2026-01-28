import sqlite3
from .db import get_connection


def run_migrations():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS ojt_logs(
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        time_in TIME NOT NULL,
        time_out TIME NOT NULL,
        remarks TEXT NOT NULL,
        hours_rendered INT NOT NULL);
        """)
    con.commit()
    con.close()


def add_log(date, time_in, time_out, remarks):
    hours_rendered = 6
    con = get_connection()
    stmt = """INSERT INTO ojt_logs(date, time_in,time_out,remarks,hours_rendered)
    VALUES(?,?,?,?,?)"""

    cur = con.cursor()
    cur.execute(stmt, (date, time_in, time_out, remarks, hours_rendered))
    con.commit()
    con.close()


def list_logs():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM ojt_logs")
    rows = cur.fetchall()
    con.close()
    return rows
