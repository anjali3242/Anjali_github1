# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type' , 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!this is my python web application.')

httpd = HTTPServer(('',PORT), MyHandler)
print(f'Serving on port {PORT}...')
httpd.serve_forever()
