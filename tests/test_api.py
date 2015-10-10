# coding: utf-8
import os
import unittest
import zaim

class TestApi(unittest.TestCase):
    def setUp(self):
        consumer_key = os.environ.get("ZAIM_CONSUMER_KEY", "")
        consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET", "")
        access_token = os.environ.get("ZAIM_ACCESS_TOKEN", "")
        access_token_secret = os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", "")
        assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
        assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
        assert access_token, 'Please set "ZAIM_ACCESS_TOKEN".'
        assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

        self.api = zaim.Api(consumer_key, consumer_secret, access_token, access_token_secret)

    def test_verify(self): 
        self.assertIn('me', self.api.verify().keys())

    def test_money(self):
        response = self.api.money()
        self.assertIn('money', response.keys())

    def test_category(self): 
        response = self.api.category()
        self.assertIn('categories', response.keys())

    def test_genre(self): 
        response = self.api.genre()
        self.assertIn('genres', response.keys())

    def test_account(self): 
        self.assertIn('accounts', self.api.account().keys())

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

    def test_payment(self): 
        self.__payment()
        response = self.api.money(
            mapping=1,
            category_id='101',
            genre_id='10101',
            mode='payment',
            start_date='2020-04-01',
            end_date='2020-04-01')
        self.assertTrue(len(response['money']) > 0)
        for tran in response['money']:
            self.api.delete('payment', tran['id'])
    
    def test_update(self): 
        response = self.__payment()
        response = self.api.update('payment', response['money']['id'], 
            amount=1,
            date='2020-04-01',
            place='updated place',
            name='updated name',
            comment='updated comment')
        self.assertIn('money', response.keys())
        self.api.delete('payment', response['money']['id'])

if __name__ == '__main__':
   unittest.main() 
