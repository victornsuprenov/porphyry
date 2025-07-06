document.addEventListener('DOMContentLoaded', function() {
    // Получаем все элементы
    const elements = {
        formTitle: document.getElementById('form-title'),
        submitBtn: document.getElementById('submit-btn'),
        switchBtn: document.getElementById('switch-btn'),
        emailGroup: document.getElementById('email-group'),
        authForm: document.getElementById('auth-form'),
        messageDiv: document.getElementById('message'),
        usernameInput: document.getElementById('username'),
        passwordInput: document.getElementById('password'),
        emailInput: document.getElementById('email')
    };

    // Проверяем наличие всех элементов
    for (const [key, element] of Object.entries(elements)) {
        if (!element) {
            console.error(`Элемент ${key} не найден!`);
            return;
        }
    }

    let isLogin = new URLSearchParams(window.location.search).get('action') === 'login';

    // Функция обновления формы
    function updateForm() {
        if (isLogin) {
            elements.formTitle.textContent = 'Вход';
            elements.submitBtn.textContent = 'Войти';
            elements.switchBtn.textContent = 'Зарегистрироваться';
            elements.emailGroup.style.display = 'none';
            elements.emailInput.removeAttribute('required');
        } else {
            elements.formTitle.textContent = 'Регистрация';
            elements.submitBtn.textContent = 'Зарегистрироваться';
            elements.switchBtn.textContent = 'Войти';
            elements.emailGroup.style.display = '';
            elements.emailInput.setAttribute('required', '');
        }
    }

    // Обработчик кнопки переключения
    elements.switchBtn.addEventListener('click', function(e) {
        e.preventDefault();
        isLogin = !isLogin;
        updateForm();
        elements.messageDiv.textContent = '';
        elements.messageDiv.className = 'error';
    });

    // Обработчик отправки формы
    elements.authForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        elements.messageDiv.textContent = '';
        elements.messageDiv.className = 'error';

        const formData = {
            username: elements.usernameInput.value,
            password: elements.passwordInput.value
        };

        if (!isLogin) {
            formData.email = elements.emailInput.value;
        }

        try {
            const response = await fetch(isLogin ? '/login' : '/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                elements.messageDiv.textContent = result.message;
                elements.messageDiv.className = 'success';
                setTimeout(() => window.location.href = '/', 1000);
            } else {
                elements.messageDiv.textContent = result.message || 'Ошибка';
                elements.messageDiv.className = 'error';
            }
        } catch (err) {
            elements.messageDiv.textContent = 'Ошибка соединения';
            elements.messageDiv.className = 'error';
            console.error('Ошибка:', err);
        }
    });

    // Инициализация формы
    updateForm();
});