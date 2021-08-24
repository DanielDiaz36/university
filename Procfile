release: python manage.py migrate; python manage.py load
web: gunicorn app.wsgi --log-file -