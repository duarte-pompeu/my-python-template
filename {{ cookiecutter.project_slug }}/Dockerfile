# inspired by https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287
{# FIXME: dont duplicate this #}
{% set python_version_tuples = cookiecutter.python_version.split(".") -%}
{% if python_version_tuples|length != 3 %}{% include "error" ~ " Invalid python version. Valid example: '3.11.1'." %}{% endif -%}
{% set python_version_major, python_version_minor, python_version_patch = python_version_tuples %}



FROM python:{{ python_version_major }}.{{ python_version_minor}}-slim

# install poetry and dependencies
WORKDIR /{{ cookiecutter.project_slug }}
RUN pip3 install poetry==1.1.13
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install --no-dev

# copy assets
COPY ./assets ./assets

# copy the code
COPY ./{{ cookiecutter.project_slug }} ./{{ cookiecutter.project_slug }} 
ENV PYTHONPATH=.${PYTHONPATH}:${PWD}


# run the program
ENTRYPOINT ["python3", "{{ cookiecutter.project_slug }}/main.py"]
