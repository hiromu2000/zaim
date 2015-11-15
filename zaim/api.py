# -*- coding: utf-8 -*-
"""Python bindings for the Zaim API"""
try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl
import requests
from requests_oauthlib import OAuth1

import logging
logging.captureWarnings(True)

class Api(object):
    """A wrapper class for the Zaim API"""
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        if consumer_key is not None and consumer_secret is not None:
            self.consumer_key = consumer_key
            self.consumer_secret = consumer_secret
            if access_token is not None and access_token_secret is not None:
                self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    def __post(self, path, **kwargs):
        r = requests.post(u"https://api.zaim.net/v2" + path, auth=self.auth, data=kwargs)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(r.text)

    def __get(self, path, **kwargs):
        if hasattr(self, 'auth'):
            r = requests.get(u"https://api.zaim.net/v2" + path, auth=self.auth, params=kwargs)
        else:
            r = requests.get(u"https://api.zaim.net/v2" + path, params=kwargs)
        try:
            return r.json()
        except ValueError:
            raise Exception(r.text)

    def __put(self, path, **kwargs):
        r = requests.put(u"https://api.zaim.net/v2" + path, auth=self.auth, data=kwargs)
        try:
            return r.json()
        except ValueError:
            raise Exception(r.text)

    def __delete(self, path):
        r = requests.delete(u"https://api.zaim.net/v2" + path, auth=self.auth)
        try:
            return r.json()
        except ValueError:
            raise Exception(r.text)

    def get_request_token(self, callback_uri):
        auth = OAuth1(self.consumer_key, self.consumer_secret, callback_uri=callback_uri)
        r = requests.post("https://api.zaim.net/v2/auth/request", auth=auth)
        request_token = dict(parse_qsl(r.text))
        self.request_token = request_token['oauth_token']
        self.request_token_secret = request_token['oauth_token_secret']
        return request_token

    def get_access_token(self, oauth_verifier):
        auth = OAuth1(self.consumer_key, self.consumer_secret,
                      self.request_token, self.request_token_secret,
                      verifier=oauth_verifier)
        r = requests.post("https://api.zaim.net/v2/auth/access", auth=auth)
        access_token = dict(parse_qsl(r.text))
        self.auth = OAuth1(self.consumer_key,
                           self.consumer_secret,
                           access_token['oauth_token'],
                           access_token['oauth_token_secret'])
        return access_token

    def verify(self):
        return self.__get(u"/home/user/verify")

    def money(self, mapping=1, category_id=None, genre_id=None,
              mode=None, order=None, start_date=None, end_date=None,
              page=None, limit=None, group_by=None):
        return self.__get(u"/home/money",
                          mapping=1, category_id=category_id, genre_id=genre_id,
                          mode=mode, order=order, start_date=start_date,
                          end_date=end_date, page=page, limit=limit,
                          group_by=group_by)

    def account(self):
        return self.__get(u"/home/account")

    def category(self):
        return self.__get(u"/home/category")

    def genre(self):
        return self.__get(u"/home/genre")

    def default_account(self):
        return self.__get(u"/account")

    def default_category(self):
        return self.__get(u"/category")

    def default_genre(self):
        return self.__get(u"/genre")

    def default_currency(self):
        return self.__get(u"/currency")

    def payment(self, mapping=1, category_id=None, genre_id=None,
                amount=None, date=None, from_account_id=None,
                comment=None, name=None, place=None):
        return self.__post(u"/home/money/payment",
                           mapping=1, category_id=category_id, genre_id=genre_id,
                           amount=amount, date=date, from_account_id=from_account_id,
                           comment=comment, name=name, place=place)

    def income(self, mapping=1, category_id=None, amount=None,
               date=None, to_account_id=None, comment=None, place=None):
        return self.__post(u"/home/money/income",
                           mapping=1, category_id=category_id, amount=amount,
                           date=date, to_account_id=to_account_id, comment=comment,
                           place=place)

    def transfer(self, mapping=1, amount=None, date=None,
                 from_account_id=None, to_account_id=None, comment=None):
        return self.__post(u"/home/money/transfer",
                           mapping=1, amount=amount, date=date,
                           from_account_id=from_account_id, to_account_id=to_account_id, comment=comment)

    def delete(self, mode, money_id):
        return self.__delete(u"/home/money/%s/%d" % (mode, money_id))

    # 'place' and 'name' can be updated, despite not explictily stated in https://dev.zaim.net
    def update(self, mode, money_id, mapping=1, amount=None, place=None, name=None,
               date=None, from_account_id=None, to_account_id=None,
               genre_id=None, category_id=None, comment=None):
        return self.__put(u"/home/money/%s/%d" % (mode, money_id),
                          mapping=1, amount=amount, place=place, name=name,
                          date=date, from_account_id=from_account_id, to_account_id=to_account_id,
                          genre_id=genre_id, category_id=category_id, comment=comment)
