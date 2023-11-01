// language.js

function changeLanguage(languageCode) {
    // Отправляем AJAX-запрос на сервер с выбранным языком
    var csrftoken = getCookie('csrftoken'); // Получаем CSRF-токен
    // console.log('CSRF Token:', csrftoken); // Выводим токен CSRF в консоль, только тест!!!, при первой загрузке страницы вызывает ошибку из-за отсутствия csrftoken

    // Устанавливаем атрибуты SameSite и Secure для куки csrftoken
    document.cookie = 'csrftoken=' + csrftoken + '; path=/; SameSite=None; Secure';

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/i18n/setlang/', true);
    xhr.setRequestHeader('X-CSRFToken', csrftoken); // Установите CSRF-токен
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Обработка успешного ответа, например, обновление страницы
            location.reload();
        }
    };
    xhr.send('language=' + languageCode);
}

// Функция для получения CSRF-токена из куки
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Ищем куки с нужным именем
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                // console.log('cookieValue:', cookieValue); // Выводим токен CSRF в консоль
                break;
            }
        }
    }
    return cookieValue;
}
