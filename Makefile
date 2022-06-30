install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff

full:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall
