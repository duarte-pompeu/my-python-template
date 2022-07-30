# inspired by https://gist.github.com/trickeydan/0bace38b00ba8488b5aa1f178b1f3f33
# and https://blog.mathieu-leplatre.info/tips-for-your-makefile-with-python.html
# and https://venthur.de/2021-03-31-python-makefiles.html

.DEFAULT_GOAL:=help

SOURCE:=app
TESTS:=tests
EXTRA:=extra
ALL_CODE := $(SOURCE) $(TESTS) $(EXTRA)

INSTALL_STAMP := .venv/.install.stamp


ifndef POETRY_ACTIVE 
    $(warning Tip: Activate a poetry shell to run makefile targets faster: around 1 second per command) 
    CMD := poetry run 
endif

install: $(INSTALL_STAMP) ## install the project dependencies in a virtual environment
$(INSTALL_STAMP): poetry.lock pyproject.toml 
	poetry lock
	poetry install
	touch $(INSTALL_STAMP)

.PHONY: run
run: $(INTALL_STAMP)  ## runs the python application
	PYTHONPATH=. $(CMD) dotenv -f .env run -- python app/main.py

.PHONY: clean
clean: ## removes files generated during installation or compilation
	rm -rf .venv
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete


.PHONY: all
all: format lint test cov ## formats, lints and tests

.PHONY: tall ## checks types and all targets
tall: type all

.PHONY: format
format: $(INSTALL_STAMP) ## Formats the code and sorts imports consistently
	PYTHONPATH=. $(CMD) black $(ALL_CODE) 
	PYTHONPATH=. $(CMD) isort --profile=black $(ALL_CODE)

.PHONY: lint
lint: $(INSTALL_STAMP) ## Analyzes the code and reports inconsistencies
	PYTHONPATH=. $(CMD) flake8 $(SOURCE) $(EXTRA) --extend-ignore=E501
	PYTHONPATH=. $(CMD) pylint --disable=all --enable=W1505,W0402,W0110,E,F --extension-pkg-whitelist=pydantic $(SOURCE) 

.PHONY: type
type: $(INSTALL_STAMP) ## checks types in code
	$(CMD) mypy $(ALL_CODE)

.PHONY: test
test: $(INSTALL_STAMP) ## run tests
	PYTHONPATH=. $(CMD) coverage run  --source=$(SOURCE)/ -m pytest $(TESTS)

.PHONY: cov
cov: $(INSTALL_STAMP) ## gets test coverage for previous test run
	$(CMD) coverage report 


# inspired by https://gist.github.com/prwhite/8168133#gistcomment-2833138
help: ## Displays help message (this)
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
