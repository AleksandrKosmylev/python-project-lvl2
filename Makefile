install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-lvl2  --cov-report xml

lint:
	poetry run flake8 python-project-lvl2

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build

