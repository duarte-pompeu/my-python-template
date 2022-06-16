# my-python-template

A minimalistic, but opinionated, Python template using pyenv and poetry.

## Requirements

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

## Running an example webserver

```bash
make run
```

The webserver should be accessible now at http://localhost:8000.

## Running with docker

```bash
docker compose up
```

The webserver should be accessible now at http://localhost:8000.


## Running with kubernetes

```bash
docker build --tag "docker.io/library/my-python-project:latest" .
kubectl apply --filename kubernetes/
```

If you want to see the results, you can use port-forwarding:

```
kubectl port-forward services/my-python-project 8000:80
```

And now you can validate the deployment at http://localhost:8000.

## Help

If you're a beginner, this may not be the best template for you. But if you still want to give it a go, we can simplify it:

- ignore `pyenv`, delete it from `setup.sh`
- change pyproject.toml to the python version you have

Beginner or not, if you're not interested in infrastructure, you can ignore everything related to docker, kubernetes, helm, ci/cd.
