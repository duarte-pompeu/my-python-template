import config
from webserver import WebServer

config.setup()

print("Hello, world!")
print(f"Example from config: {config.settings.example}")

# implement a web server using only the standard library
# just do display docker and kubernetes working
server = WebServer()
server.run()
