#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='simple-md-server',
    version='0.1.0',
    description="A basic example of using Python' SocketServer & SimpleHTTPRequestHandler to convert Markdown documents to HTML on the fly.",
    long_description=readme,
    author='Randle Taylor',
    author_email='randle.taylor@gmail.com',
    url='https://github.com/randlet/simple-md-server',
    packages=[
        'simple-md-server',
    ],
    package_dir={'simple-md-server': 'simple-md-server'},
    scripts=['servemd.py'],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='simple-md-server',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
