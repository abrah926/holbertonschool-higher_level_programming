import http.server
import json
from urllib.parse import urlparse


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif parsed_path.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'name': 'John', 'age': 30, 'city': 'New York'}
            self.wfile.write(json.dumps(data).encode())

        elif parsed_path.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {'status': 'OK'}
            self.wfile.write(json.dumps(status).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {'error': 'Endpoint not found'}
            self.wfile.write(json.dumps(error_message).encode())

    def log_message(self, format, *args):
        return


def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
