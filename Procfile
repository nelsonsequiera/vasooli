web:python manage.py runserver
web:python manage.py migrate
web:python manage.py collectstatic
web: gunicorn vasooli.wsgi --log-file -
heroku ps:scale web=1