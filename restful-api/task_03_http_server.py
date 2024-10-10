#!/usr/bin/python3
"""
Simple HTTP Server

This module sets up a basic HTTP server
using Python's http.server module. It handles GET requests
and returns responses based on the requested endpoint.

Endpoints:
- "/": Returns a simple text message.
- "/data": Returns a JSON response with sample data.
- "/status": Returns a JSON response with an OK status message.
- Default: Returns a 404 Not Found status for undefined endpoints.
"""

import http.server
import socketserver
import json

PORT = 8000


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests.
    """

    def do_GET(self):
        """
        Routes GET requests to specific endpoints.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


Handler = SimpleHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
