import sqlite3
import json
from contextlib import contextmanager
from .config import settings

SCHEMA = '''
CREATE TABLE IF NOT EXISTS users (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 email TEXT UNIQUE NOT NULL,
 name TEXT NOT NULL,
 password_hash TEXT NOT NULL,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS recommendations (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_id INTEGER,
 planner TEXT NOT NULL,
 budget REAL NOT NULL,
 input_json TEXT NOT NULL,
 result_json TEXT NOT NULL,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(user_id) REFERENCES users(id)
);
'''

@contextmanager
def get_db():
    conn = sqlite3.connect(settings.database_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with get_db() as db:
        db.executescript(SCHEMA)

def create_user(email, name, password_hash):
    with get_db() as db:
        cur = db.execute('INSERT INTO users(email,name,password_hash) VALUES(?,?,?)', (email, name, password_hash))
        return cur.lastrowid

def get_user_by_email(email):
    with get_db() as db:
        return db.execute('SELECT * FROM users WHERE lower(email)=lower(?)', (email,)).fetchone()

def get_user(user_id):
    with get_db() as db:
        return db.execute('SELECT id,email,name,created_at FROM users WHERE id=?', (user_id,)).fetchone()

def save_recommendation(user_id, planner, budget, inputs, result):
    with get_db() as db:
        cur = db.execute('INSERT INTO recommendations(user_id,planner,budget,input_json,result_json) VALUES(?,?,?,?,?)',
                         (user_id, planner, budget, json.dumps(inputs), json.dumps(result)))
        return cur.lastrowid

def get_history(user_id, limit=50):
    with get_db() as db:
        rows = db.execute('SELECT * FROM recommendations WHERE user_id=? ORDER BY id DESC LIMIT ?', (user_id, limit)).fetchall()
        return [dict(r) for r in rows]

def get_recommendation(user_id, rec_id):
    with get_db() as db:
        row = db.execute('SELECT * FROM recommendations WHERE id=? AND user_id=?', (rec_id, user_id)).fetchone()
        return dict(row) if row else None
