# my-python-template

A minimalistic, but opinionated, Python template using pyenv and poetry.

# Requirements

- [Poetry](https://python-poetry.org/docs/#installation)
- [Pyenv](https://github.com/pyenv/pyenv#installation)

## Installing

```bash
bash setup.sh
```

## Configuration

Populate `.env`, which is not version controlled to:
- enable different people to use different configs
- avoid exposing sensible configurations, eg passwords

## Running an example app

```bash
make run
```

## Help

If you're a beginner, you can ignore `pyenv`: delete it from setup and just use whatever python version you have installed.

If you're not interested in infrastructure, you can ignore everything related to docker, kubernetes, helm, ci/cd.