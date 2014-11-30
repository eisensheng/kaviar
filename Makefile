.PHONY: docs
.SILENT: init-devel test test-tox test-coverage

all: clean test

clean-docs:
	-rm -rfv docs/_build

clean-tox:
	-rm -rfv .tox

clean-coverage:
	-rm .coverage*
	-rm coverage.xml
	-rm -rfv htmlcov

clean-pyc:
	-find . -path './.tox' -prune -or \
		-name '__pycache__' -exec rm -rv {} +
	-find . -path './.tox' -prune -or \
		\( -name '*.pyc' -or -name '*.pyo' \) -exec rm -rv {} +

clean-all: clean-tox clean-docs clean

clean: clean-pyc clean-coverage
	-rm -rv build dist *.egg-info

init-devel:
	pip install -r requirements/develop.txt

test:
	py.test -v tests

test-tox:
	tox

test-coverage:
	coverage erase
	coverage run --source=kaviar --branch -m pytest -v
	coverage report
	coverage xml

audit:
	flake8 kaviar

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

docs:
	$(MAKE) -C docs html

doctest:
	$(MAKE) -C docs doctest
