from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

addr = '0.0.0.0'
port = 8084

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('COntent-type','text/html')
        self.end_headers()

        content = "<html><body>Hello world</body></html>"

        self.wfile.write(bytes(content, 'utf-8'))
        return

class ThreadedHTTPServer(ThreadingMixIn, Handler):
    pass

def main():
    try:
        server = ThreadedHTTPServer((addr, port), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting server')
        server.socket.close()


if __name__ == '__main__':
    main()
