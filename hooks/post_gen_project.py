import os

license = "{{ cookiecutter.license }}"
if license == "Not open source":
    os.remove("LICENSE")
