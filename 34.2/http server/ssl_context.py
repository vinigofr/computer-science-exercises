# import ssl
# from http.server import HTTPServer, BaseHTTPRequestHandler


# ssl_context = ssl.SSLContext()
# ssl_context.load_cert_chain('cert.pem', 'key.pem')

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b'Hello, world!')


# httpd = HTTPServer(('localhost', 4000), SimpleHTTPRequestHandler)
# httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
# httpd.serve_forever().

import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

ssl_context = ssl.SSLContext()
ssl_context.load_cert_chain("cert.pem", keyfile="key.pem")

httpd = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()