import config
from webserver import WebServer

config.setup()

print("Hello, world!")
print(f"Example from config: {config.settings.example}")

# implement a web server using only the standard library
# just so we can show some results in docker and kubernetes
server = WebServer()
server.run()
