import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
print('id | username | email | password_hash')
print('-' * 70)
for row in cursor.execute('SELECT id, username, email, password FROM users'):
    print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
conn.close()
