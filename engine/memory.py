# TODO: Add encryption for sensitive user data
# TODO: Implement long-term conversation summaries

import sqlite3

def init_db():
    """Creates the database and memory table if they don't exist."""
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS memory 
                      (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

def update_memory(key, value):
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def get_memory(key):
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM memory WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_all_memory():
    """Returns all key-value pairs from memory as a dictionary."""
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM memory")
    rows = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}