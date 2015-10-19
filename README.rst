zaim
====

Python bindings for the Zaim API.
This also includes a command-line script (``zaim``).

How to use
==========

For functions requiring no authentication

.. code-block:: python

    >>> import zaim
    >>> api = zaim.Api()
    >>> api.default_account()


For functions requiring authentication

.. code-block:: python

    >>> import zaim
    >>> api = zaim.Api(consumer_key='consumer_key',
                       consumer_secret='consumer_secret',
                       access_token='access_token',
                       access_token_secret='access_token_secret')
    >>> api.verify()
    >>> response = api.payment(category_id='101',
                               genre_id='10101',
                               amount=1,
                               date='2020-04-01',
                               comment='comment',
                               name='name',
                               place='place',
                               from_account_id=0)
    >>> api.money(mapping=1,
                  mode='payment',
                  start_date='2020-04-01',
                  end_date='2020-04-01')
    >>> api.delete(mode='payment',
                   money_id=response['money']['id'])

For extended functions

.. code-block:: python

    >>> import zaim
    >>> api = zaim.ExtendedApi(consumer_key='consumer_key',
                               consumer_secret='consumer_secret',
                               access_token='access_token',
                               access_token_secret='access_token_secret')
    >>> response = api.payment(category_id='101',
                               genre_id='10101',
                               amount=1,
                               date='2020-04-01',
                               comment='comment',
                               name='name',
                               place='place',
                               from_account_id=0)
    >>> api.search(mapping=1,
                   mode='payment',
                   place='place',
                   name='name',
                   comment='comment')
    >>> api.delete(mode='payment',
                   money_id=response['money']['id'])
    >>> api.category_from_name(u'食費')
    >>> api.genre_from_name(u'カフェ')

How to use the command-line script
==================================

.. code-block:: bash

    $ export ZAIM_CONSUMER_KEY="YOUR CONSUMER KEY"
    $ export ZAIM_CONSUMER_SECRET="YOUR CONSUMER SECRET"
    $ zaim token_get --callback-uri http://example.com

How to develop
==============

Test
----

.. code-block:: bash

    $ cd /path/to/zaim
    $ export PYTHONPATH=$PYTHONPATH:/path/to/zaim/zaim
    $ python tests/test_zaim_no_auth.py

    $ export ZAIM_CONSUMER_KEY=consumer_key
    $ export ZAIM_CONSUMER_SECRET=consumer_secret
    $ export ZAIM_ACCESS_TOKEN=access_token
    $ export ZAIM_ACCESS_TOKEN_SECRET=access_token_secret
    $ python tests/test_api.py
    $ python tests/test_extended_api.py

or simply

.. code-block:: bash

    $ sudo pip install tox
    $ cd /path/to/zaim
    $ export ZAIM_CONSUMER_KEY=consumer_key
    $ export ZAIM_CONSUMER_SECRET=consumer_secret
    $ export ZAIM_ACCESS_TOKEN=access_token
    $ export ZAIM_ACCESS_TOKEN_SECRET=access_token_secret
    $ tox

Build
-----

.. code-block:: bash

    $ python setup.py sdist
    $ python setup.py bdist_wheel --universal

ToDo
----

- Documentation (written in Sphinx (reST) and hosted in readthedocs)
- Enrich the command-line script

Acknowledgements
================

- A part of the codes is originally from `here <https://github.com/konomae/zaimpy>`_.
