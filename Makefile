ENV = .env
virtualenv=. $(ENV)/bin/activate
PYTHON=python3.6

install:
	$(virtualenv); pip install --upgrade setuptools;
	$(virtualenv); pip install --no-cache-dir -r requirements/dev.txt

virtualenv:
	virtualenv $(ENV) -p $(PYTHON) || true
	$(virtualenv); pip install --upgrade setuptools virtualenv

migrate:
	$(virtualenv); python src/manage.py migrate --database=default