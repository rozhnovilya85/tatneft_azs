Используемые модули и библиотеки приведенны в файле
requirements.txt

Для первоначального заполнения базы данных (СУБД PostgreSQL Django) запускаем скрипт:
python manage.py tatneft
Для обновления раз в месяц данных списков АЗС с сайта rss.tatneft.ru используем переодическую задачу на базе Celery
используем команды:
-redis-server
-celery -A tatneft_azs beat
-celery -A tatneft_azs worker -l info --pool=solo

API ключ
url = 'http://localhost:8000/api/tatneftazs/'

