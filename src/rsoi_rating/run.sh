python3 manage.py makemigrations rsoi_rating_app
python3 manage.py migrate
python3 manage.py loaddata data
python3 manage.py runserver 0.0.0.0:$PORT
