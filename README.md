Elon shop - [ССЫЛКА](http://185.195.26.199/)
---

### Про проект:

Я решил по фану сделать типа магазин. В проекте реализован каталог товаров,
блог, профиль с корзиной, форма для получения обратной связи,
авторизация + регистрация + выход из аккаунта и типа покупка товара.

Сайт поставлен на хостинг [ССЫЛКА](http://185.195.26.199/)

Все уведомления обратной связи и "типа покупки" приходит
в [КАНАЛ]([ССЫЛКА](http://185.195.26.199/)

Проект написан на python + django 3.2.16

Инструкция по установке
---

#### 1)Клонируем репозиторий

    git clone https://github.com/Badsnus/django_shop

#### 2)Создаем виртуальное окружение и активируем его

    python -m venv venv

    Windows: venv\Scripts\activate.bat
    Linux и MacOS: source venv/bin/activate

#### 3)Заходим в директорию репозитория

    cd django_shop

#### 4) Устанавливаем зависимости

    pip install -r requirements.txt

#### 5)Заходим в директорию джанго проекта

    cd ELONSHOP

#### 6) .env.example -> .env

    В lyceum_django_lessons есть файл .env.example его нужно переименовать в .env 

#### 7) Делаем миграции

    python manage.py migrate

#### 8) Загружаем данные из бд (ну можно и не загружать)

    python manage.py loaddata data.json

Данные от superuser:

    legenda
    passwOASRA1231af

#### 9) Start

    python manage.py runserver

