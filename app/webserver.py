from wsgiref.simple_server import make_server
from wsgiref import util
import random
from loguru import logger

class WebServer:
    def run(self):
        def simple_app(environ, start_response):
           
            status = "200 OK"
            headers = [("Content-type", "image/jpg")]

            start_response(status, headers)
            i = random.randint(1,3)
            path = f"assets/simba_pantera_{i}.jpg"
            return util.FileWrapper(open(path, "rb"))

        with make_server("", 8000, simple_app) as httpd:
            logger.info("Serving on port 8000...")
            httpd.serve_forever()
