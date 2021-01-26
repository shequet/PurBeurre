from django.core.management.base import BaseCommand, CommandError
from purbeurre.openfoodfact import OpenFoodFacts
from purbeurre.models import Brand, Category, Product, ProductBrand, ProductCategory, ProductStore, Store


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
                         and 'nutriscore_score' in product\
                         and 'image_front_url' in product:

                    nutriscore_score = openFoodFacts.decode_nutriscore(product['nutriscore_score'])

                    if nutriscore_score is not None:
                        dbProduct, createdProduct = Product.objects.update_or_create(
                            code=product['code'],
                            defaults={
                                'name': product['product_name_fr'].strip(),
                                'nutri_score': nutriscore_score,
                                'link': product['url'] if 'url' in product and product['url'] != '' else None,
                                'quantity': product['quantity'] if 'quantity' in product else None,
                                'image': product['image_front_url'] if 'image_front_url' in product else None,
                            },
                        )

                        if 'categories' in product:
                            for category in product['categories'].split(','):
                                category = category.strip()
                                if category != '':
                                    dbCategory, createdCategory = Category.objects.get_or_create(
                                        name=category,
                                        defaults={
                                            'name': category
                                        },
                                    )
                                    ProductCategory.objects.get_or_create(
                                        product=dbProduct,
                                        category=dbCategory
                                    )

                        if 'brands' in product:
                            for brand in product['brands'].split(','):
                                brand = brand.strip()
                                if brand != '':
                                    dbBrand, createdBrand = Brand.objects.get_or_create(
                                        name=brand,
                                        defaults={
                                            'name': brand
                                        },
                                    )
                                    ProductBrand.objects.get_or_create(
                                        product=dbProduct,
                                        brand=dbBrand
                                    )

                        if 'stores' in product:
                            for store in product['stores'].split(','):
                                store = store.strip()
                                if store != '':
                                    dbStore, createdStore = Store.objects.get_or_create(
                                        name=store,
                                        defaults={
                                            'name': store
                                        },
                                    )
                                    ProductStore.objects.get_or_create(
                                        product=dbProduct,
                                        store=dbStore
                                    )

