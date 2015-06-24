#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='facebook-python-sdk',
    version='0.1.1',
    description='This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, which is the canonical way to implement Facebook authentication.',
    author='Facebook',
    url='http://github.com/eventbrite/facebook-python-sdk',
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.4',
    ],
    py_modules=[
        'facebook',
    ],
)
