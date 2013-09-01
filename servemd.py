#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import markdown2
import os
import SocketServer
import StringIO
import sys

from SimpleHTTPServer import SimpleHTTPRequestHandler


MARKDOWN_EXTENSIONS = ["md", "markdown"]

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset=utf-8>
    <style>
      body { }
      html,body { margin:0; padding:0; }

    body {
        font-family: "Lucida Grande", Tahoma, Arial, Helvetica, sans-serif;
        text-align:justify;
        margin-top: 20px;
        color: #444;
    }

    div#content{
        width:80%%;
        max-width:700px;
        margin:0 auto;
        text-align:justify;
    }

    </style>
  </head>
  <body>
    <div id="content">%s</div>
  </body>
"""


class MDRequestHandler(SimpleHTTPRequestHandler):

    #---------------------------------------------------------------
    def do_GET(self, *args, **kwargs):
        """
        Respond to a request, converting Markdown to html on the fly
        if requested file has a markdown extension
        """

        is_markdown = any(self.path.endswith(e) for e in MARKDOWN_EXTENSIONS)

        if is_markdown:
            f = self.send_markdown()
        else:
            # if not a mardkown file just use default RequestHandler behaviour
            f = self.send_head()

        if f:
            self.copyfile(f, self.wfile)
            f.close()

    #---------------------------------------------------------------
    def send_markdown(self):
        """
        Handle requests for md documents.  Read in the markdown file and
        convert it to html using markdown2.
        """

        path = self.translate_path(self.path)

        try:
            mdf = open(path, 'rb')
            content = TEMPLATE % (markdown2.markdown(mdf.read()))
            f = StringIO.StringIO(content)
        except IOError:
            self.send_error(404, "File not found")
            return None

        self.send_response(200)
        encoding = sys.getfilesystemencoding()

        self.send_header("Content-type", "text/html; charset=%s" % encoding)

        fs = os.fstat(mdf.fileno())

        self.send_header("Content-Length", "%d" % (f.len))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f


def run(root, port):

    os.chdir(root)
    httpd = SocketServer.TCPServer(("", port), MDRequestHandler)

    print "serving %s at port: %d\nCtrl+C to Quit" % (root, port)
    httpd.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A simple Markdown document server")
    parser.add_argument('--root', "-r", default="./", help="Root directory to serve from")
    parser.add_argument('--port', "-p", default=8000, type=int, help="port to run the server on")

    args = parser.parse_args()

    if os.path.isdir(args.root):
        run(args.root, args.port)
    else:
        print "not a valid directory"
