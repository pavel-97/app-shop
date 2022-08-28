#Интернет-магазин

##1. Коротко о проекте
    
Интернет-магазин реализовас с помощью фреймврка Django. В приложении
реализованы следующие возможности:
    1. Просмотр, коментирование и покупка товаров.
    2. Авторизация, регистрация.
    3. Для удобства больших покупок есть карзина.
    4. Онлайн заказ с возможностью доставки на дом.
    5. Поиск товара по сайту.
    6. Сортировка товара.

##2. Установка проекта

1. Установить инструмент pipenv:

        Для Ubuntu:
        sudo apt install software-properties-common python-software-properties
        sudo add-apt-repository ppa:pypa/ppa
        sudo apt update
        sudo apt install pipenv

        Для Windows:
        pip install --user pipenv

        Для MacOS:
        brew install pipenv

2. Перейдите в директорию проекта и выполните следуюшию команду:
        pipenv sync --dev
        
        При деплои проекта:
        pipenv sync

3. Выполните миграции:
        pipenv run python manage.py migrate
    
4. Запустите проект:
        pipenv run python manage.py runserver