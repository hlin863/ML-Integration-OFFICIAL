#! /bin/sh

# User credentials
user=admin
email=admin@example.com
password=pass

python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$user').exists() or User.objects.create_superuser('$user', '$email', '$password')"

exec python manage.py runserver 0.0.0.0:8000
