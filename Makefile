mig:
	python3 manage.py makemigrations --settings=root.settings_dev
	python3 manage.py migrate --settings=root.settings_dev

rm-mig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "./.venv/*" -delete
	find . -path "*/migrations/*.pyc" -not -path "./.venv/*" -delete

user:
	python3 manage.py createsuperuser

req:
	pip3 freeze > requirements.txt

load:
	python3 manage.py loaddata country region district hosting_tariffs ssl_tariffs


celery:
	celery -A root worker -l INFO