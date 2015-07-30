# coding: utf-8
import os
import unittest
from zaim import Zaim

class TestZaim(unittest.TestCase):
    def setUp(self):
        consumer_key = os.environ.get("ZAIM_CONSUMER_KEY", "")
        consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET", "")
        access_token = os.environ.get("ZAIM_ACCESS_TOKEN", "")
        access_token_secret = os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", "")
        assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
        assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
        assert access_token, 'Please set "ZAIM_ACCESS_TOKEN".'
        assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

        self.zaim = Zaim(consumer_key, consumer_secret, access_token, access_token_secret)

    def test_verify(self): 
        self.assertIn('me', self.zaim.verify().keys())

    def test_money(self):
        response = self.zaim.money()
        self.assertIn('money', response.keys())

    def test_category(self): 
        response = self.zaim.category()
        self.assertIn('categories', response.keys())

    def test_genre(self): 
        response = self.zaim.genre()
        self.assertIn('genres', response.keys())

    def test_account(self): 
        self.assertIn('accounts', self.zaim.account().keys())

    def test_currency(self): 
        self.assertIn('currencies', self.zaim.currency().keys())

    def __payment(self):
        response = self.zaim.payment(
            category_id='101',
            genre_id='10101',
            amount=1,
            date='2020-04-01',
            comment='comment',
            name='name',
            place='place')
        return response

    def test_payment(self): 
        response = self.__payment()
        self.assertIn('money', response.keys())
        self.zaim.delete('payment', response['money']['id'])
    
    def test_update(self): 
        response = self.__payment()
        response = self.zaim.update('payment', response['money']['id'], 
            amount=1,
            date='2020-04-01',
            comment='updated comment')
        self.assertIn('money', response.keys())
        self.zaim.delete('payment', response['money']['id'])

if __name__ == '__main__':
   unittest.main() 
