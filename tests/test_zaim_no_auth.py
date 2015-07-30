# coding: utf-8
import unittest
import zaim

class TestZaimNoAuth(unittest.TestCase):
    def setUp(self):
        self.api = zaim.Api()

    def test_default_account(self):
        self.assertIn('accounts', self.api.default_account().keys())

    def test_default_category(self):
        self.assertIn('categories', self.api.default_category().keys())

    def test_default_genre(self):
        self.assertIn('genres', self.api.default_genre().keys())

    def test_default_currency(self):
        self.assertIn('currencies', self.api.default_currency().keys())

if __name__ == '__main__':
   unittest.main()
