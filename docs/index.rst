requests_nzgovtmbie
=============

This package allows for authentication to the NZ Government MBIE BusinessData services using the requests library.
It is an example of HMAC based authenication being used to access protected REST end points.

Usage
-----

``HttpNzgovtmbieAuth`` extends requests ``AuthBase``, so usage is simple:
    Default output is json, to output xml set via the Headers, see 2nd example below:

.. code:: python

    import requests
    from requests_nzgovtmbie import HttpNzgovtmbieAuth
    r = requests.get("http://eat.businessdata.govt.nz/data/app/ws/rest/companies/role/search/v1.0/acme", auth=HttpNzgovtmbieAuth("key", "secret"))

    headers = {'Accept': 'application/xml'}
    r = requests.get("http://eat.businessdata.govt.nz/data/app/ws/rest/companies/role/search/v1.0/jones bob", headers=headers, auth=HttpNzgovtmbieAuth(k, s))

Installation
------------

The package hasn't been uploaded to pip yet, but it can be installed by 
running::

    sudo python ./setup.py install

Requirements
------------

- requests


Authors
-------

- `Chris Esther`_

.. _Chris Esther: https://github.com/cesther
