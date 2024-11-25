import http.server
import socketserver

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("<my ip>", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
 
