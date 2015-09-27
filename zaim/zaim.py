# coding: utf-8
import requests
from requests_oauthlib import OAuth1

class Api(object):
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        if not (consumer_key is None or consumer_secret is None or access_token is None or access_token_secret is None):
            self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    def __post(self, path, params):
        r = requests.post(u"https://api.zaim.net/v2" + path, auth=self.auth, data=params)
        return r.json()

    def __get(self, path, params=""):
        if hasattr(self, 'auth'):
            r = requests.get(u"https://api.zaim.net/v2" + path, auth=self.auth, params=params)
        else:
            r = requests.get(u"https://api.zaim.net/v2" + path, params=params)
        return r.json()

    def __put(self, path, params=""):
        r = requests.put(u"https://api.zaim.net/v2" + path, auth=self.auth, data=params)
        return r.json()

    def __delete(self, path):
        r = requests.delete(u"https://api.zaim.net/v2" + path, auth=self.auth)
        return r.json()

    def verify(self):
        return self.__get(u"/home/user/verify")

    def money(self, **params):
        return self.__get(u"/home/money", params)

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

    def payment(self, **params):
        return self.__post(u"/home/money/payment", params)

    def income(self, **params):
        return self.__post(u"/home/money/income", params)

    def transfer(self, **params):
        return self.__post(u"/home/money/transfer", params)

    def delete(self, mode, money_id):
        return self.__delete(u"/home/money/%s/%d" % (mode, money_id))

    def update(self, mode, money_id, **params):
        return self.__put(u"/home/money/%s/%d" % (mode, money_id), params)

    def search(self, **params):
        response = self.__get(u"/home/money", params)
        for tran in response['money'][:]:
            for key in ['amount', 'from_account_id', 'to_account_id', 'place', 'name', 'comment']:
                if key in params.keys():
                    if tran[key] != params[key]:
                        response['money'].remove(tran)
        return response
