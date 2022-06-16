import config
from webserver import WebServer

config.setup()

print("Hello, world!")
print(f"Example from config: {config.settings.example}")

server = WebServer()
server.run()
