import sqlite3

CONN = sqlite3.connect(':memory:')  # or use 'db/development.db' for a file-based DB
CURSOR = CONN.cursor()
