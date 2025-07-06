# database.py
import sqlite3
import os
from contextlib import contextmanager

DATABASE_NAME = 'database.db'

def init_db():
    """Инициализация базы данных"""
    if not os.path.exists(DATABASE_NAME):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()

@contextmanager
def get_db_connection():
    """Контекстный менеджер для работы с соединением к БД"""
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def get_db_cursor():
    """Контекстный менеджер для работы с курсором БД"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except:
            conn.rollback()
            raise