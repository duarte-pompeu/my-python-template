from {{ cookiecutter.project_slug }} import config, webserver

config.setup()

print("Hello, world!")
print(f"Example from config: {config.general.example}")

# implement a web server using only the standard library
# just so we can show some results in docker and kubernetes
server = webserver.WebServer()
server.run()
