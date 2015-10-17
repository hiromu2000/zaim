# -*- coding: utf-8 -*-
from .api import Api

class ExtendedApi(Api):
    def search(self, place=None, name=None, comment=None, amount=None,
               to_account_id=None, from_account_id=None,
               money_id=None, user_id=None, active=None, receipt_id=None,
               created=None, currency_code=None,
               mapping=1, category_id=None, genre_id=None,
               mode=None, order=None, start_date=None, end_date=None,
               page=None, limit=None, group_by=None):
        response = self.money(mapping=1, category_id=category_id, genre_id=genre_id,
                              mode=mode, order=order, start_date=start_date,
                              end_date=end_date, page=page, limit=limit,
                              group_by=group_by)
        trans = []
        for tran in response['money']:
            if money_id is not None and tran['id'] != money_id:
                    continue
            if user_id is not None and tran['user_id'] != user_id:
                    continue
            if to_account_id is not None and tran['to_account_id'] != to_account_id:
                    continue
            if from_account_id is not None and tran['from_account_id'] != from_account_id:
                    continue
            if amount is not None and tran['amount'] != amount:
                    continue
            if active is not None and tran['active'] != active:
                    continue
            if name is not None and tran['name'] != name:
                    continue
            if receipt_id is not None and tran['receipt_id'] != receipt_id:
                    continue
            if place is not None and tran['place'] != place:
                    continue
            if created is not None and tran['created'] != created:
                    continue
            if currency_code is not None and tran['currency_code'] != currency_code:
                    continue
            trans.append(tran)
        response['money'] = trans
        return response

    def search_category(self, name=None, category_id=None, mode=None,
                        sort=None, parent_category_id=None, active=None,
                        modified=None):
        response = self.category()
        categories = []
        for category in response['categories']:
            if category_id is not None and category['id'] != category_id:
                    continue
            if name is not None and category['name'] != name:
                    continue
            if mode is not None and category['mode'] != mode:
                    continue
            if sort is not None and category['sort'] != sort:
                    continue
            if parent_category_id is not None and category['parent_category_id'] != parent_category_id:
                    continue
            if active is not None and category['active'] != active:
                    continue
            if modified is not None and category['modified'] != modified:
                    continue
            categories.append(category)
        response['categories'] = categories
        return response

    def search_genre(self, name=None, genre_id=None, sort=None,
                     active=None, category_id=None, parent_genre_id=None,
                     modified=None):
        response = self.genre()
        genres = []
        for genre in response['genres']:
            if genre_id is not None and genre['id'] != genre_id:
                    continue
            if name is not None and genre['name'] != name:
                    continue
            if sort is not None and genre['sort'] != sort:
                    continue
            if active is not None and genre['active'] != active:
                    continue
            if category_id is not None and genre['category_id'] != category_id:
                    continue
            if parent_genre_id is not None and genre['parent_genre_id'] != parent_genre_id:
                    continue
            if modified is not None and genre['modified'] != modified:
                    continue
            genres.append(genre)
        response['genres'] = genres
        return response

    def search_account(self, name=None, account_id=None, mode=None,
                       sort=None, parent_account_id=None, active=None,
                       modified=None):
        response = self.account()
        accounts = []
        for account in response['accounts']:
            if account_id is not None and account['id'] != account_id:
                    continue
            if name is not None and account['name'] != name:
                    continue
            if mode is not None and account['mode'] != mode:
                    continue
            if sort is not None and account['sort'] != sort:
                    continue
            if parent_account_id is not None and account['parent_account_id'] != parent_account_id:
                    continue
            if active is not None and account['active'] != active:
                    continue
            if modified is not None and account['modified'] != modified:
                    continue
            accounts.append(account)
        response['accounts'] = accounts
        return response
