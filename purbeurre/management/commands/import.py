from django.core.management.base import BaseCommand, CommandError
from purbeurre.openfoodfact import OpenFoodFacts
from purbeurre.models import Category, Product


class Command(BaseCommand):
    """
    Command to import products
    """

    help = 'Importing products from OpenFoodFacts'

    def add_arguments(self, parser):
        parser.add_argument('categories', nargs='+', type=str)

    def search_nutriment(self, product, key):
        """
        Search if the element is present
        """

        if 'nutriments' in product and key in product['nutriments']:
            return float(product['nutriments'][key])
        return None

    def handle(self, *args, **options):
        """
        Command processing
        """

        for category in options['categories']:
            openFoodFacts = OpenFoodFacts()
            products = openFoodFacts.get_category(category)

            for product in products:

                if 'product_name_fr' in product \
                         and product['product_name_fr'] != ""\
                         and product['code'] != ""\
                         and 'nutriscore_score' in product\
                         and product['nutriscore_score'] != ""\
                         and 'image_front_url' in product\
                         and 'categories' in product\
                         and product['categories_lc'] == 'fr':

                    category_name = product['categories'].split(',')[-1].strip()
                    category, created_category = Category.objects.get_or_create(
                        name=category_name,
                        defaults={
                            'name': category_name
                        },
                    )

                    Product.objects.update_or_create(
                        code=product['code'],
                        defaults={
                            'name': product['product_name_fr'].strip(),
                            'nutri_score': openFoodFacts.decode_nutriscore(product['nutriscore_score']),
                            'eco_score': product['ecoscore_grade'] if 'ecoscore_grade' in product else None,
                            'link': product['url'] if 'url' in product and product['url'] != '' else None,
                            'quantity': product['quantity'] if 'quantity' in product else None,
                            'image': product['image_front_url'] if 'image_front_url' in product else None,
                            'category': category,
                            'nutriment_energy': self.search_nutriment(product, 'energy_100g'),
                            'nutriment_sugars': self.search_nutriment(product, 'sugars_100g'),
                            'nutriment_salt': self.search_nutriment(product, 'salt_100g'),
                            'nutriment_fat': self.search_nutriment(product, 'fat_100g'),
                            'nutriment_saturated_fat': self.search_nutriment(product, 'saturated-fat_100g'),
                            'nutriment_sodium': self.search_nutriment(product, 'sodium_100g'),
                            'nutriment_proteins': self.search_nutriment(product, 'proteins_100g'),
                            'nutriment_carbohydrates': self.search_nutriment(product, 'carbohydrates_100g'),
                            'nutriment_fiber': self.search_nutriment(product, 'fiber_100g'),
                        },
                    )
