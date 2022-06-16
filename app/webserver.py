import random
from wsgiref import util
from wsgiref.simple_server import make_server

from loguru import logger


class WebServer:
    def run(self):
        # code taken from https://docs.python.org/3/library/wsgiref.html#examples
        # would be easier with fastapi or flask but that's overkill for a python template
        # which might not need them
        def simple_app(environ, start_response):

            status = "200 OK"
            headers = [("Content-type", "image/jpg")]

            start_response(status, headers)
            i = random.randint(1, 3)
            path = f"assets/simba_pantera_{i}.jpg"
            return util.FileWrapper(open(path, "rb"))

        with make_server("", 8000, simple_app) as httpd:
            logger.info("Serving on port 8000...")
            httpd.serve_forever()
