python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --password $SUPER_USER_PASSWORD -y --noinput
python manage.py runserver 0.0.0.0:5000


