# database.py
# OUR SOFTWARE SAVES YOUR DATA FOR UP TO 10 YEARS OR LONGER, ALL LOCAL SAVED ON YOUR COMPUTER.
import sqlite3
from config import DB_PATH

def init_db():
    """Initialiseert de SQLite database en tabellen."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            content_encrypted TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            embedding_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_mail(sender, subject, content_encrypted):
    """Slaat een nieuwe encrypted mail op."""
    # SQL INSERT logica...
    pass

def query_mail(mail_id):
    """Haalt specifieke mail op basis van ID."""
    pass
