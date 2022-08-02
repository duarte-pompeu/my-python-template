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


Populate `env/app.env` for your configuration. An example is available at `env/example.env`.

`env/app.env` is not versioned control because this:

- lets different people to use different configs
- avoids exposing sensible configurations, eg passwords

## Running the application

```bash
make run
```

The webserver should be accessible now at http://localhost:8000.

## Running with docker

```bash
docker compose up
```

The containerized webserver should be accessible now at http://localhost:8000.

## Running with kubernetes

```bash
docker build --tag "docker.io/library/my-python-project:latest" .
kubectl apply --filename kubernetes/
```

If you want to see the results, you can use port-forwarding:

```
kubectl port-forward services/my-python-project 8000:80
```

And now you can validate your orchestration at http://localhost:8000.

## Help

If you're a beginner, this may not be the best template for you. But if you still want to give it a go, we can simplify it:

- ignore `pyenv`, delete it from `setup.sh`
- change pyproject.toml to the python version you have

Additionally, if you're not interested in infrastructure, you can ignore everything related to docker, kubernetes, helm, ci/cd.
