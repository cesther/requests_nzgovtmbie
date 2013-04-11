#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

with open('LICENSE','r') as f:
  license = f.read().strip()

setup(
    name         = 'requests_nzgovtmbie',
    version      = '0.0.6',
    packages     = [ 'requests_nzgovtmbie' ],
    requires     = [ 'requests(>=1.0.0)'],
    provides     = [ 'requests_nzgovtmbie' ],
    author       = 'Chris Esther',
    author_email = 'cesther@zetzea.com',
    description  = 'This package allows for authentication to the NZ Government MBIE BusinessData services using the requests library.',
    license      = license
)
