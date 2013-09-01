===============================
Simple Markdown Server
===============================

A basic example of using Python's SocketServer & SimpleHTTPRequestHandler. In this case 
the server is used to convert Markdown documents to HTML on the fly.

* Free software: BSD license

Installation
------------

These install instructions will put servemd.py in your Python Scripts directory
meaning servemd.py should be in your $PATH after installation.


| git clone https://github.com/randlet/simple-md-server
| cd simple-md-server
| python setup.py install

Features
--------

* Serves local .md & .markdown files as html by using the markdown2 library to convert them on the fly.
* There are no other features :)

Usage
-----

For usage instructions

servemd.py -h

