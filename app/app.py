# app.py
from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from database import init_db, get_db_cursor
import sqlite3  # Добавляем импорт sqlite3
import os

app = Flask(__name__, static_folder='static')

# Инициализация БД при старте приложения
init_db()

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Регистрация
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Обработка как JSON, так и form-data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({"message": "Все поля обязательны"}), 400
        
        hashed_password = generate_password_hash(password)

        try:
            with get_db_cursor() as cursor:
                cursor.execute(
                    'INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                    (username, email, hashed_password)
                )
            return jsonify({"message": "Пользователь создан"}), 201
        except sqlite3.IntegrityError as e:
            error_msg = "Пользователь уже существует"
            if "email" in str(e):
                error_msg = "Email уже используется"
            return jsonify({"message": error_msg}), 400
        except Exception as e:
            return jsonify({"message": f"Ошибка сервера: {str(e)}"}), 500
    
    return render_template('register.html')

# Вход
@app.route('/login', methods=['POST'])
def login():
    # Обработка как JSON, так и form-data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
        
    username = data.get('username')
    password = data.get('password')

    try:
        with get_db_cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()

        if user and check_password_hash(user[3], password):
            return jsonify({"message": "Успешный вход"}), 200
        else:
            return jsonify({"message": "Неверные данные"}), 401
    except Exception as e:
        return jsonify({"message": f"Ошибка сервера: {str(e)}"}), 500

# Страница "О проекте"
@app.route('/info')
def info():
    return render_template('info.html')

# Страница "Контакты"
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)