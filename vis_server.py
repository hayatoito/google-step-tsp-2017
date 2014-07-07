#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import os

PORT = 800

class NoCacheHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def __init__(self, request, client_address, server):
    SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server);

  def send_head(self):
    #copy-pasta from SimpleHTTPServer source:
    path = self.translate_path(self.path)
    f = None
    if os.path.isdir(path):
        for index in "index.html", "index.htm":
            index = os.path.join(path, index)
            if os.path.exists(index):
                path = index
                break
        else:
            return self.list_directory(path)
    ctype = self.guess_type(path)
    if ctype.startswith('text/'):
        mode = 'r'
    else:
        mode = 'rb'
    try:
        f = open(path, mode)
    except IOError:
        self.send_error(404, "File not found")
        return None
    self.send_response(200)
    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate");
    self.send_header("Pragma", "no-cache");
    self.send_header("Expires", "0");
    self.send_header("Content-type", ctype)
    self.end_headers()
    return f

Handler = NoCacheHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
