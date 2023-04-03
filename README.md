# Duarte's Python Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to generate an opinionated Python template according to [duarte-pompeu](https://github.com/duarte-pompeu) preferences.
It includes:

- pre-defined package requirements managed by poetry
- Makefile with utilities, such as `make format`, `make lint` and `make test`
- minimalistic support for docker and kubernetes

To initialize a project with this template:

1. Install cookiecutter (if you don't have it yet)
2. Install the project
3. Run `setup.sh` to configure [poetry](https://github.com/python-poetry/poetry) and [pyenv](https://github.com/pyenv/pyenv)

## 1 - Install cookiecutter

I recommend installing with pipx (but pip also works):

```bash
pipx install cookiecutter
```

## 2 - Initialize the project

```bash
cookiecutter https://github.com/duarte-pompeu/my-python-template
```

## 3 - Run `setup.sh`

```bash
bash setup.sh
```