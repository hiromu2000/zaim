# coding: utf-8
import json
import requests
from requests_oauthlib import OAuth1

class Zaim:
    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        self.__auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    def getClient(self):
        token    = oauth2.Token(key=self.__access_token, secret=self.__access_token_secret)
        consumer = oauth2.Consumer(key=self.__consumer_key, secret=self.__consumer_secret)
        return oauth2.Client(consumer, token)

    def access(self, method, url, params=""):
        resp, content = self.client.request(url, method=method, body=urlencode(params))
        print resp,content
        return json.loads(content)

    def post(self, path, params):
        r = requests.post(u"https://api.zaim.net/v2" + path, auth=self.__auth, data=params)
        return r.json()

    def get(self, path, params=""):
        r = requests.get(u"https://api.zaim.net/v2" + path, auth=self.__auth, data=params)
        return r.json()

    def verify(self):
        return self.get(u"/home/user/verify")

    def money(self):
        return self.get(u"/home/money")

    def account(self):
        return self.get(u"/home/account")

    def category(self):
        return self.get(u"/home/category")

    def genre(self):
        return self.get(u"/home/genre")

    def currency(self):
        return self.get(u"/currency")

    def payment(self, category_id, genre_id, amount, date, comment, name, place):
        params = {
                'category_id'     : category_id,
                'genre_id'        : genre_id,
                'amount'          : amount,
                'comment'         : comment,
                'name'            : name,
                'date'            : date,
                'place'           : place,
                'from_account_id' : 1,
                #'receipt_id'      : receipt_id,
            }
        return self.post(u"/home/money/payment", params)

    def income(self, category_id, amount, date, comment):
        params = {
                'category_id'   : category_id,
                'amount'        : amount,
                'date'          : date,
                'to_account_id' : money_bug,
                'comment'       : comment,
            }
        return self.post(u"/home/money/income", params)
