#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import subprocess
from sys import platform

# HTTPServer is a socketserver.TCPServer subclass. It creates and
# listens at the HTTP socket, dispatching the requests to a handler.
#
# BaseHTTPRequestHandler is used to handle the HTTP requests that
# arrive at the server. By itself, it cannot respond to any actual
# HTTP requests; it must be subclassed to handle each request method
# (e.g. GET or POST).  BaseHTTPRequestHandler provides a number of
# class and instance variables, and methods for use by subclasses.

host = "192.168.1.109"
port = 8080
html = "<html><head><title>Welcome!</title></head><body><h1>Hello.</h1></body></html>"


class WebServer(BaseHTTPRequestHandler):
    """dispatcher"""

    def do_GET(self):
        if platform.startswith('win32'):
            is_windows = True

        """Respond to a GET request."""
        if self.path == "/":
            # HTTP 200 Found
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
        elif self.path == "/text":
            self.send_response(200)
            self.wfile.write("Greetings.\nIsn't this nice?\n".encode())

        elif self.path == "/date":
            self.send_response(200)
            if is_windows:
                p = subprocess.run( ("date","/t"), shell=True, capture_output=True)
            else:
                p = subprocess.run("date", capture_output= True)
            date_result = p.stdout.decode()
            self.wfile.write(date_result.encode())

        elif self.path == "/date/seconds":
            self.send_response(200)
            now = time.time()
            year, month, day, hh, mm, ss, x, y, z = time.localtime(now)
            s = f"{now}"
            self.wfile.write(s.encode())
        else:
        # HTTP 404 Not Found
            self.send_error(404)

httpd = HTTPServer((host, port), WebServer)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
