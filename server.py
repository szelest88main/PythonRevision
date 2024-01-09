# requires pip (dependencies)
#!/usr/bin/env python3
# usage: something like http://localhost:8080/tujestcos?siabdama
# -> SplitResult(scheme='', netloc='', path='/tujestcos', query='siabdama', fragment='')

"""
License: MIT License
Copyright (c) 2023 Miel Donkers
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit
import logging

class S(BaseHTTPRequestHandler):
    def create_or_append(self, line):
        # open a file to write:
        file_descriptor = open('data.txt','a', encoding='utf-8')
        file_descriptor.write(line+"\n") # write the line
        file_descriptor.close() # close

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        #logging.info('Ctrl+C!\n')
        #logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        boinkval = urlsplit(self.path)
        #print("###########")
        #print(boinkval)  # Prints None or the string value of imsijkjkk
        if(boinkval.path == "/tujestcos"):
            print("received data=" + boinkval.query)
        #print("###########")
        logging.info('Ctrl+C!\n')

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    logging.info('Ctrl+C!\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
