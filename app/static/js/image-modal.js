document.addEventListener('DOMContentLoaded', function() {
    // Создаем модальное окно
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.id = 'imageModal';
    modal.innerHTML = `
        <span class="close-btn">&times;</span>
        <img src="" alt="" class="modal-content" id="modalImage">
    `;
    document.body.appendChild(modal);

    // Получаем элементы
    const modalImg = document.getElementById('modalImage');
    const closeBtn = document.querySelector('.close-btn');

    // Добавляем обработчики для всех изображений с классом thumbnail
    document.querySelectorAll('.thumbnail').forEach(img => {
        img.addEventListener('click', function() {
            modalImg.src = this.src;
            modalImg.alt = this.alt;
            modal.style.display = 'flex';
            document.body.classList.add('modal-open');
        });
    });

    // Закрытие модального окна
    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) closeModal();
    });

    function closeModal() {
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
    }

    // Закрытие по ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            closeModal();
        }
    });
});
