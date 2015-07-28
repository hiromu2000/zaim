# coding: utf-8
import os
import unittest
from zaim import Zaim

class TestZaim(unittest.TestCase):
    def setUp(self):
        consumer_key = unicode(os.environ.get("ZAIM_CONSUMER_KEY", ""))
        consumer_secret = unicode(os.environ.get("ZAIM_CONSUMER_SECRET", ""))
        access_token = unicode(os.environ.get("ZAIM_ACCESS_TOKEN", ""))
        access_token_secret = unicode(os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", ""))
        assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
        assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
        assert access_token, 'Please set "ZAIM_ACCESS_TOKEN".'
        assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

        self.zaim = Zaim(consumer_key, consumer_secret, access_token, access_token_secret)

    def test_verify(self): 
        self.assertIn('me', self.zaim.verify().keys())

    def test_money(self):
        self.assertIn('money', self.zaim.money().keys())

    def test_category(self): 
        self.assertIn('categories', self.zaim.category().keys())

    def test_genre(self): 
        self.assertIn('genres', self.zaim.genre().keys())

    def test_account(self): 
        self.assertIn('accounts', self.zaim.account().keys())

    def test_currency(self): 
        self.assertIn('currencies', self.zaim.currency().keys())

if __name__ == '__main__':
   unittest.main() 
