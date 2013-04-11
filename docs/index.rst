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
    requests.get("http://ntlm_protected_site.com",auth=HttpNtlmAuth('domain\\username','password'))

Installation
------------

The package hasn't been uploaded to pip yet, but it can be installed by 
running::

    sudo python ./setup.py install

Requirements
------------

- requests_
- python-ntlm_

.. _requests: https://github.com/kennethreitz/requests/
.. _python-ntlm: http://code.google.com/p/python-ntlm/

Authors
-------

- `Chris Esther`_

.. _Chris Esther: https://github.com/cesther
