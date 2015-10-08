# coding: utf-8
import os
import unittest
import zaim

class TestExtendedApi(unittest.TestCase):
    def setUp(self):
        consumer_key = os.environ.get("ZAIM_CONSUMER_KEY", "")
        consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET", "")
        access_token = os.environ.get("ZAIM_ACCESS_TOKEN", "")
        access_token_secret = os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", "")
        assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
        assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
        assert access_token, 'Please set "ZAIM_ACCESS_TOKEN".'
        assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

        self.api = zaim.ExtendedApi(consumer_key, consumer_secret, access_token, access_token_secret)

    def __payment(self):
        response = self.api.payment(
            category_id='101',
            genre_id='10101',
            amount=1,
            date='2020-04-01',
            comment='comment',
            name='name',
            place='place',
            from_account_id=0)
        return response

    def test_search(self):
        response = self.__payment()
        money_id = response['money']['id']
        response = self.api.search(
            mode='payment',
            amount=1,
            from_account_id=0,
            comment='comment',
            place='place',
            name='name')
        self.assertTrue(len(response['money']) == 1)
        self.api.delete('payment', money_id)

    def test_search_category(self):
        response = self.api.category()
        response = self.api.search_category(name=response['categories'][0]['name'])
        self.assertTrue(len(response['categories']) > 0)

    def test_search_genre(self):
        response = self.api.genre()
        response = self.api.search_genre(name=response['genres'][0]['name'])
        self.assertTrue(len(response['genres']) > 0)

    def test_search_account(self):
        response = self.api.account()
        response = self.api.search_account(name=response['accounts'][0]['name'])
        self.assertTrue(len(response['accounts']) > 0)

if __name__ == '__main__':
   unittest.main() 
