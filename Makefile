install:
	poetry install

test:
	poetry run pytest tests/test_gendiff.py

test-coverage:
	poetry run pytest --cov=tests --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
