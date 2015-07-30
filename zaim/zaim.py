# coding: utf-8
import requests
from requests_oauthlib import OAuth1

class Api(object):
    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        self.__auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    def __post(self, path, params):
        r = requests.post(u"https://api.zaim.net/v2" + path, auth=self.__auth, data=params)
        return r.json()

    def __get(self, path, params=""):
        r = requests.get(u"https://api.zaim.net/v2" + path, auth=self.__auth, data=params)
        return r.json()

    def __put(self, path, params=""):
        r = requests.put(u"https://api.zaim.net/v2" + path, auth=self.__auth, data=params)
        return r.json()

    def __delete(self, path):
        r = requests.delete(u"https://api.zaim.net/v2" + path, auth=self.__auth)
        return r.json()

    def verify(self):
        return self.__get(u"/home/user/verify")

    def money(self):
        return self.__get(u"/home/money")

    def account(self):
        return self.__get(u"/home/account")

    def category(self):
        return self.__get(u"/home/category")

    def genre(self):
        return self.__get(u"/home/genre")

    def currency(self):
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
