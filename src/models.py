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
