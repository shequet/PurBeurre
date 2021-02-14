#! /usr/bin/env python3
# coding: utf-8
""" OpenFoodFacts class """
import requests
from django.conf import settings


class OpenFoodFacts:
    """ OpenFoodFacts class """

    def __init__(self):
        self.url = settings.OPENFOODFACTS_URL

    def get_category(self, category):
        """ get products for category"""

        return self.call_api('{url}/categorie/{category}.json'.format(
            url=self.url,
            category=category))

    def decode_nutriscore(self, nutri_score):
        """ Decode nutriscore """

        if nutri_score < -1:
            return 'A'
        elif 0 <= nutri_score <= 2:
            return 'B'
        elif 3 <= nutri_score <= 10:
            return 'C'
        elif 11 <= nutri_score <= 18:
            return 'D'
        elif nutri_score >= 19:
            return 'E'
        else:
            return 'E'

    def call_api(self, url, page=1, products=[]):
        """ Call Api open food facts"""

        r = requests.get(
            url,
            params={
                'page': page,
                'page_size': settings.OPENFOODFACTS_PAGE_SIZE
            })

        if r.status_code == 200 and r.json is not None:

            data = r.json()
            if len(data['products']) > 0:
                products.extend(data['products'])
                print('--Page:[{page}]--Total products:[{products}]--'.format(
                    page=page,
                    products=len(products)))
                return self.call_api(
                    url=url,
                    page=int(data['page']) + 1,
                    products=products)

        return products
