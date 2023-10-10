.PHONY: create-$(VENV) activate run install-reqs db-init db-clean ruff flake8 lint

.DEFAULT_GOAL := run

# The system's python interpreter. Used only to create virtual environment.
PY = python3

# The name of the virtual environment.
VENV = blog-venv

# The path to the virtual environment's bin or Scripts directory.
BIN = $(VENV)/bin

# Adding support to Windows.
ifeq ($(OS), Windows_NT)
    PY = python
    BIN = $(VENV)/Scripts
endif

PIP = $(BIN)/pip
PYTHON = $(BIN)/$(PY)
ACTIVATE = $(BIN)/activate

# For some reason, the globstar (eg, **/*.py) is broken in windows. This is a workaround.
# Source: https://stackoverflow.com/questions/2483182/recursive-wildcards-in-gnu-make
# Other: https://dev.to/blikoor/customize-git-bash-shell-498l
rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

create-$(VENV): requirements.txt requirements-dev.txt
	@echo "Creating virtual environment..."
	$(PY) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) install --upgrade -r requirements-dev.txt
	@echo "Done."

activate: $(VENV)
	@echo "Activating virtual environment..."
	. ./$(ACTIVATE)
	@echo "Done."

run: $(VENV)
	@echo "Running..."
	$(PYTHON) src/run.py
	@echo "Done."

install-reqs: $(VENV) requirements.txt requirements-dev.txt
	@echo "Installing requirements..."
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) install --upgrade -r requirements-dev.txt
	@echo "Done."

db-init: $(VENV)
	@echo "Initializing database..."
	# $(PYTHON) src/db_init.py
	$(PYTHON) -c "import os; os.chdir('src'); import db_init; db_init.init_db()"
	@echo "Done."

db-clean: $(VENV) src/instance/site.db
	@echo "Clearing database..."
	$(PYTHON) -c "import os; os.chdir('src'); import db_init; db_init.drop_db()"
	@echo "Done."

ruff: $(VENV)
	@echo "Linting Python files using ruff..."
	$(BIN)/ruff .
	@echo "Done."

flake8: $(VENV)
	@echo "Linting Python files using flake8..."
	$(BIN)/flake8 --color always
	@echo "Done."

lint: ruff flake8
