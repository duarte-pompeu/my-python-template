import os

{% if cookiecutter.license ==   "Not open source"%}
os.remove("LICENSE")
{% endif %}

{% if cookiecutter.docker_and_kubernetes in [False, "False", "false"] %}
os.remove("Dockerfile")
os.remove("docker-compose.yaml")

for file in os.listdir("kubernetes"):
    os.remove(f"kubernetes/{file}")
os.rmdir("kubernetes")
{% endif %}
