from django.core.management.base import BaseCommand, CommandError
from purbeurre.openfoodfact import OpenFoodFacts
from purbeurre.models import Product


class Command(BaseCommand):
    help = 'Importing products from OpenFoodFacts'

    def add_arguments(self, parser):
        parser.add_argument('categories', nargs='+', type=str)

    def handle(self, *args, **options):
        for category in options['categories']:
            openFoodFacts = OpenFoodFacts()
            products = openFoodFacts.get_category(category)

            for product in products:

                if 'product_name_fr' in product \
                         and product['product_name_fr'] != ""\
                         and product['code'] != ""\
                         and 'nutriscore_score' in product\
                         and product['nutriscore_score'] != ""\
                         and 'image_front_url' in product:

                    dbProduct, created = Product.objects.update_or_create(
                        code=product['code'],
                        defaults={
                            'name': product['product_name_fr'],
                            'nutri_score': openFoodFacts.decode_nutriscore(product['nutriscore_score']),
                            'link': product['url'] if 'url' in product and product['url'] != '' else None,
                            'quantity': product['quantity'] if 'quantity' in product else None,
                            'image': product['image_front_url'] if 'image_front_url' in product else None,
                        },
                    )
