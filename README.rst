zaim
====

.. image:: https://travis-ci.org/hiromu2000/zaim.svg?branch=master
    :target: https://travis-ci.org/hiromu2000/zaim

.. image:: https://img.shields.io/pypi/dm/zaim.svg
    :target: https://pypi.python.org/pypi/zaim

Python bindings for the Zaim API.
This also includes a command-line script (``zaim``).

How to install
==============

.. code-block:: bash

    $ pip install zaim

or

.. code-block:: bash

    $ git clone https://github.com/hiromu2000/zaim
    $ python setup.py install

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
    >>> api.search_category(u'食費')
    >>> api.search_genre(u'カフェ')
    >>> api.search_account(u'銀行')

How to use the command-line script
==================================

.. code-block:: bash

    $ export ZAIM_CONSUMER_KEY="YOUR CONSUMER KEY"
    $ export ZAIM_CONSUMER_SECRET="YOUR CONSUMER SECRET"
    $ zaim token_get --callback-uri http://example.com

.. code-block:: bash

    $ export ZAIM_CONSUMER_KEY=consumer_key
    $ export ZAIM_CONSUMER_SECRET=consumer_secret
    $ export ZAIM_ACCESS_TOKEN=access_token
    $ export ZAIM_ACCESS_TOKEN_SECRET=access_token_secret
    $ zaim money
    $ zaim payment --category-id 101 --genre-id 10101 --amount 1 --place 'place'
                   --date '2020-04-01' --comment 'comment' --name 'name'
    $ zaim delete --mode payment --money-id XXXXXXXXX

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
- Argument validation for CLI (e.g., account-id)

Acknowledgements
================

- A part of the codes is originally from `here <https://github.com/konomae/zaimpy>`_.
