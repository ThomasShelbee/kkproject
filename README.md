# kkproject


1. Введение
Название: Магазин одежды KK clothing
Описание: Сайт, на котором покупатель сможет выбрать понравившуюся ему вещь, добавить в корзину и затем приобрести
Целевая аудитория: Аудитория из Telegram-канала KK clothing, подписчики канала в социальной сети TikTok


3. Анализ требований
Функциональные требования:
1) Просмотр каталога товаров СДЕЛАНО
2) Возможность перехода на страницу с подробным описанием вещи СДЕЛАНО
3) Добавление в корзину и оформление заказа СДЕЛАНО
4) Онлайн-оплата на сайте В РАЗРАБОТКЕ

Нефункциональные требования:
1) Должно работать на мобильных и десктопных устройствах. СДЕЛАНО
2) Предполагается иметь сервер не на Tilda, а написанный своими руками СДЕЛАНО
3) Динамичный эффект заднего фона на сайте. В РАЗРАБОТКЕ


3. Концепция пользовательского интерфейса (UI/UX)
Основные страницы:
1) Главная страница (каталог и простенькая менюшка с разделами: О нас, Доставка). МЕНЮ В РАЗРАБОТКЕ
2) Отдельная страница для каждого товара (фото, цена, описание). СДЕЛАНО
3) Страница “Доставка” с текстовым разъяснением способов доставки(возможно не понадобится, если получиться подключить CDEK) В РАЗРАБОТКЕ
4) Страница с корзиной (фото, описание, цена и кол-во вещей находящихся там) СДЕЛАНО
5) Страница оформления заказа(Поля для ввода необходимой нам информации) СДЕЛАНО
6) Страница “О нас” с кратким описанием нашего бренда, возможно альбомом фото и нашей контактной информацией В РАЗРАБОТКЕ

Пользовательские сценарии:
Человек заходит на сайт, листает каталог в поиске интересующей его вещи, переходит на страницу с подробным описанием товара, добавляет вещь в корзину и оформляет заказ на нее. УЖЕ РЕАЛИЗУЕМО
Человек заходит на сайт с целью узнать наш бренд получше, переходит на страницу “О нас”, где находит интересующую его информацию. ЕЩЕ НЕ РЕАЛИЗУЕМО


4. Архитектура системы
Технологии:
1) Frontend: Vue.js (для динамичного интерфейса).
2) Backend: Flask (обрабатывает запросы, хранит данные).
3) База данных: Flask SQL Alchemy (хранит товары и промокоды).

Структура баз данных:
1) Item (id, url, title, price, quantity, s_size, m_size, l_size, xl_size, description).
2) Promos (id, title, quantity, price).

API (основные запросы):
1) GET /get-items – получение списка постов.
2) GET /get-promos – получение списка промокодов.
3) GET /get-picture/${url} – получение картинки.
4) POST /purchase – оформление заказа.
5) DELETE /delete-promo - удаление использованного промокода из базы данных


Инструкция по запуску:
1) Сделать Сommit and Push на github всех изменений в коде.
2) Залогиниться на сервер в консоли.
3) Создать/Зайти в папку прокта.
4) Запуллить код с гитхаба (git pull).
5) Сделать сетап кода (sudo sh setup.sh)
6) По необходимости еще раз ввести пароль от профиля
7) Запустить проект (sh start.sh)

Инструкция по остановке:
1) В той же консоли прописать sh stop.sh

