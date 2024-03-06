# M10_Django

## Для проекту потрібно запустити:

```
django-admin startproject quotes_app
```

```
docker run --name quotesapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
```

Створення адміна:

```
python manage.py createsuperuser
```

Створення додатку для цитат:
```
python manage.py startapp quotes
```

Створення додатку для авторизації:

```
python manage.py startapp users
```

Міграції моделей:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Запускаємо сервер:

```
python manage.py runserver     
```

http://127.0.0.1:8000


 
## Запуск проекту

Створіть конфігураційний файл ``config.ini`` з налаштуваннями для підключення до вашої MongoDB бази даних. Ваш файл ``config.ini`` може виглядати так:

```
[mongodb]
uri = mongodb+srv://username:password@cluster.mongodb.net/mydatabase

```
