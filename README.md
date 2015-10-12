# zaim
Python bindings for the Zaim API

# How to use
For functions that require no authentication
```python
>>> import zaim
>>> api = zaim.Api()
>>> api.default_account()
```

For functions that require authentication
```python
>>> import zaim
>>> api = zaim.Api(consumer_key='consumer_key',
                   consumer_secret='consumer_secret',
                   access_token='access_token',
                   access_token_secret='access_token_secret')
>>> api.verify()
>>> response = api.payment(category_id='101', genre_id='10101', amount=1, date='2020-04-01', comment='comment', name='name', place='place', from_account_id=0)
>>> api.money(mapping=1, mode='payment', start_date='2020-04-01', end_date='2020-04-01')
>>> api.delete(mode='payment', money_id=response['money']['id'])
```

For extended functions
```python
>>> import zaim
>>> api = zaim.ExtendedApi(consumer_key='consumer_key',
                   consumer_secret='consumer_secret',
                   access_token='access_token',
                   access_token_secret='access_token_secret')
>>> response = api.payment(category_id='101', genre_id='10101', amount=1, date='2020-04-01', comment='comment', name='name', place='place', from_account_id=0)
>>> api.search(mapping=1, mode='payment', place='place', name='name', comment='comment')
>>> api.delete(mode='payment', money_id=response['money']['id'])
>>> api.category_from_name(u'食費')
>>> api.genre_from_name(u'カフェ')
```

# Test
```
$ cd /path/to/zaim
$ export PYTHONPATH=$PYTHONPATH:/path/to/zaim/zaim
$ export ZAIM_CONSUMER_KEY=consumer_key
$ export ZAIM_CONSUMER_SECRET=consumer_secret
$ export ZAIM_ACCESS_TOKEN=access_token
$ export ZAIM_ACCESS_TOKEN_SECRET= access_token_secret
$ python tests/test_api.py
$ python tests/test_extended_api.py
```

# Build
```
$ python setup.py sdist
$ python setup.py bdist_wheel --universal
```

# ToDo

- Documentation (written in Sphinx (reST) and hosted in readthedocs)
- Get the access token and secret

# Acknowledgements
- A part of the codes is originally from [here](https://github.com/konomae/zaimpy).
