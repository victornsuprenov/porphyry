# app.py
from flask import Flask, request, jsonify, redirect, url_for, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, static_folder='static')

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Регистрация
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({"message": "Все поля обязательны"}), 400

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                           (username, email, hashed_password))
            conn.commit()
            return jsonify({"message": "Пользователь создан"}), 201
        except sqlite3.IntegrityError:
            return jsonify({"message": "Пользователь уже существует"}), 400
        finally:
            conn.close()
    return render_template('register.html')


# Вход (API)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[3], password):
        return jsonify({"message": "Успешный вход"}), 200
    else:
        return jsonify({"message": "Неверные данные"}), 401

# Страница "О проекте"
@app.route('/info')
def info():
    return render_template('info.html')

# Страница "Контакты"
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
