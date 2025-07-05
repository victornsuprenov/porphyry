import sqlite3

username = input("Введите username для удаления: ")

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('DELETE FROM users WHERE username = ?', (username,))
conn.commit()
print(f"Пользователь '{username}' удалён (если существовал).")
conn.close()
