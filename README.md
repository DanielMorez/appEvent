# QUICKSTART

Прежде чем начать работу с проектом необходимо настроить:
    <br>
1. Виртуальную среду и установить необходимые библиотеки
2. MySQL
3. Docker c Redis

## Настройка виртуального окружения
Прежде чем настраивать виртуальное окружение у вас должны быть 
установлены Python 3 и python3-venv.
<br>
Если у вас нет python3-venv, вот команда для его установки:
<br>
``$ sudo apt install python3-venv``
<br>
<br>
Перейдите в корень проекта, создайте окружение и активируйте его для
дальнейшей работы в нём:
    <br>
```$ python3 -m venv venv```
    <br>
```$ source venv/bin/activate```

Теперь установим необходимые библиотеки из *requirements.txt*:
    <br>
``$ pip install -r requirements.tx``
## Установка и настройка MySQL


Если у вас уже настроена база данных MySQL, то установите свои данные в 
appEvent/setting.py
<br>
```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ИМЯ_ВАШЕЙ_БАЗЫ_ДАННЫХ',
            'USER': 'ИМЯ_ПОЛЬЗОВАТЕЛЯ',
            'PASSWORD': 'ПАРОЛЬ_ПОЛЬЗОВАТЕЛЯ',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
}
```
<br>

1. Установка сервера и консольного клиента MySQL: <br>
	```$ sudo apt-get install mysql-server mysql-client```<br>
2. Создание базы данных для работы веб-приложения Django: <br>
	```$ sudo mysql -u root -p```
3. Вы перейдете в консольный клиент MySQL. 
   Введите пароль root-пользователя, заданный в диалоговом окне на предыдущем шаге. 
   <br>В консольном клиенте введите следующую команду:<br>
   ```
    mysql> CREATE DATABASE appevent DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
	   mysql> CREATE USER django IDENTIFIED BY '123';
	   mysql> GRANT ALL PRIVILEGES ON appevent.* TO django;
	   mysql> FLUSH PRIVILEGES;
    ```
4. Нажмите Ctrl-D для выхода из консольного клиента MySQL.
5. Установка библиотек и пакетов, необходимых для работы с MySQL из Python: 
```
$ sudo apt-get install python3-dev libmysqlclient-dev build-essential
$ pip install mysqlclient
```
6. Настрока в appEvent/settings.py
```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'appevent',
            'USER': 'django',
            'PASSWORD': '123',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
}
```

## Настройка Docker & Redis
Докер понадобится для Redis. <br><br>
Чтобы установить Docker: https://docs.docker.com/engine/install/ubuntu/
<br>
После установки введите команду в терминале, чтобы поднять Redis в контейнере:
<br>
```$ sudo docker run -d -p 6379:6379 redis```
<br>
Убедитесь что redis запущен:
<br>
```$ sudo docker container ls```

Вы можете не устанавливать docker, а поднять Redis в ручную на вашей машине
(или например, на https://heroku.com)


## Запуск проекта
Сделайте миграцию в проекте:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
После успешной миграции запустите приложение:
```
python3 manage.py runserver
```
В другом окне терминала запустите worker для выполнения задачи
```
celery -A appEvent worker -l info
```
В другом окне терминала запустите beat для выполнения интервальных задач
```
celery -A appEvent beat -l info
```

Готово!

## Навигация проекта
Чтобы получить возможность сделать запрос к https://news.ycombinator.com 
перейдите по ссылке: http://127.0.0.1:8000/get-update/
<br><br>
HTTP API с методом: http://127.0.0.1:8000/posts/
<br><br>
