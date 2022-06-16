# inspired by https://gist.github.com/trickeydan/0bace38b00ba8488b5aa1f178b1f3f33

.PHONY: all path update install run clean format lint type test test-cov help
.DEFAULT_GOAL:=help

ifndef POETRY_ACTIVE 
    $(warning Tip: Activate a poetry shell to run make commands faster) 
    CMD := poetry run 
 endif

SOURCE_CODE:=app
TESTS:=tests
EXTRA_CODE:=extra
ALL_CODE := ${SOURCE_CODE} ${TESTS} ${EXTRA_CODE}

DOCKER_IMG:=my_python_app
DOCKER_CONTAINER:=$(DOCKER_IMG)
DOCKER_TAG:=latest

.PHONY: all
all: install format lint test cov ## Applys many useful targets

.PHONY: update
update: ## Updates all packages 
	poetry update

.PHONY: install
install: ## installs necessary packages
	poetry install

.PHONY: run
run:  ## runs the python application
	$(CMD) dotenv -f .env run -- python app

.PHONY: clean
clean: ## FIXME: Does nothing at the moment

format: ## Formats the code and sorts imports consistently
	$(CMD) black ${ALL_CODE} 
	$(CMD) isort --profile=black ${ALL_CODE}

lint: ## Analyzes the code and reports inconsistencies
	$(CMD) flake8 $(SOURCE_CODE) ${EXTRA_CODE} --extend-ignore=E501
	$(CMD) pylint --disable=all --enable=W1505,W0402,W0110,E,F --extension-pkg-whitelist=pydantic ${SOURCE_CODE} 

type:
	$(CMD) mypy $(SOURCE_CODE) $(TESTS) $(EXTRA_CODE)

test: ## run tests
	$(CMD) coverage run  --source=${SOURCE_CODE}/ -m pytest $(TESTS)

cov: ## gets test coverage for previous test run
	$(CMD) coverage report 




# build: ## builds a docker image with the project
# 	docker build . -t $(DOCKER_IMG):$(DOCKER_TAG)

# up: ## runs a container with the project
# 	docker container run --name $(DOCKER_CONTAINER) -i -t $(DOCKER_IMG):$(DOCKER_TAG) --rm 

# inspired by https://gist.github.com/prwhite/8168133#gistcomment-2833138
help: ## Displays help message (this)
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)