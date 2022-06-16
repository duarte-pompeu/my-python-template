# inspired by https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287

FROM python:3.10-slim

# install poetry and dependencies
WORKDIR /my-python-project
RUN pip3 install poetry==1.1.13
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install --no-dev

# copy the code
COPY ./app ./app 
ENV PYTHONPATH=.${PYTHONPATH}:${PWD}

# run the program
ENTRYPOINT ["python3", "app"]
