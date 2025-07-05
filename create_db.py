# create_db.py
import sqlite3
from werkzeug.security import generate_password_hash

# Создаем базу данных и таблицу users
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print('База данных и таблица users успешно созданы.')