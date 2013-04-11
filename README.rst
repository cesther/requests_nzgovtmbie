requests_nzgovtmbie
=============

This package allows for authentication to the NZ Govternment MBIE BusinessData services using the requests library.
It is an example of HMAC based authenication being used in accessing protected REST end points.

Usage
-----

``HttpNzgovtmbieAuth`` extends requests ``AuthBase``, so usage is simple:

.. code:: python

    import requests
    from requests_nzgovtmbie import HttpNzgovtmbieAuth
    r = requests.get("http://www.businessdata.govt.nz/data/app/ws/rest/companies/role/search/v1.0/acme", auth=HttpNzgovtmbieAuth("key", "secret)"")

Installation
------------

The package hasn't been uploaded to pip yet, but it can be installed by 
running::

    sudo python ./setup.py install

Requirements
------------

- requests_


Authors
-------

- `Chris Esther`_

.. _Chris Esther: https://github.com/cesther
