PYTHON?=python
SOURCES=codemod_json setup.py

UV:=$(shell uv --version)
ifdef UV
	VENV:=uv venv
	PIP:=uv pip
else
	VENV:=python -m venv
	PIP:=python -m pip
endif

.PHONY: venv
venv:
	$(VENV) .venv
	source .venv/bin/activate && make setup
	@echo 'run `source .venv/bin/activate` to use virtualenv'

# The rest of these are intended to be run within the venv, where python points
# to whatever was used to set up the venv.

.PHONY: setup
setup:
	$(PIP) install -Ue .[dev,test]

.PHONY: test
test:
	pytest --cov=codemod_json

.PHONY: format
format:
	ruff format
	ruff check --fix

.PHONY: lint
lint:
	ruff check $(SOURCES)
	python -m checkdeps --allow-names codemod_json codemod_json
	mypy --strict --install-types --non-interactive codemod_json

.PHONY: release
release:
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
