# coding: utf-8
import requests
from requests_oauthlib import OAuth1
from api import Api

class ExtendedApi(Api):
    def search(self, **params):
        response = self.money(**params)
        for tran in response['money'][:]:
            for key in ['amount', 'from_account_id', 'to_account_id', 'place', 'name', 'comment']:
                if key in params.keys():
                    if tran[key] != params[key]:
                        response['money'].remove(tran)
        return response

    def category_from_name(self, name):
        response = self.category()
        for category in response['categories'][:]:
            if category['name'] != name:
                response['categories'].remove(category)
        return response

    def genre_from_name(self, name):
        response = self.genre()
        for genre in response['genres'][:]:
            if genre['name'] != name:
                response['genres'].remove(genre)
        return response

    def account_from_name(self, name):
        response = self.account()
        for account in response['accounts'][:]:
            if account['name'] != name:
                response['accounts'].remove(account)
        return response
