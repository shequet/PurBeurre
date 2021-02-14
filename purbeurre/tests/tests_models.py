from django.test import TestCase
from django.contrib.auth.models import User
from purbeurre.models import Product, Category, ProductSubstitute


class TestProductModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Pâtes à tartiner aux noisettes et au cacao',
        )

    def test_product_add(self):
        product = Product.objects.create(
            name='Nutella',
            code='',
            nutri_score='E',
            link='https://fr.openfoodfacts.org/produit/80762003/nutella-ferrero',
            quantity='400 G',
            image='https://static.openfoodfacts.org/images/products/80762003/front_fr.3.400.jpg',
            category=self.category,
            nutriment_energy='2252',
            nutriment_sugars='56.3',
            nutriment_salt='0.107',
            nutriment_fat='30.9',
            nutriment_saturated_fat='10.6',
            nutriment_sodium='0.0428',
            nutriment_proteins='6.3',
            nutriment_carbohydrates='57.5',
            nutriment_fiber='7',)

        self.assertEqual(Product.objects.first(), product)

    def test_product_str(self):
        for product in Product.objects.all():
            self.assertEqual(product.__str__(), product.name)

    def test_product_delete_all(self):
        Product.objects.all().delete()
        self.assertEqual(len(Product.objects.all()), 0)


class TestCategoryModel(TestCase):

    def test_category_add(self):
        product = Product.objects.create(name='Pâtes à tartiner aux noisettes et au cacao')
        self.assertEqual(Product.objects.first(), product)

    def test_category_str(self):
        for category in Category.objects.all():
            self.assertEqual(category.__str__(), category.name)

    def test_category_delete_all(self):
        Category.objects.all().delete()
        self.assertEqual(len(Category.objects.all()), 0)


class TestProductSubstituteModel(TestCase):
    def setUp(self):
        self.username = 'test@gmail.com'
        self.password = 'password'

        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.category = Category.objects.create(
            name='Pâtes à tartiner aux noisettes et au cacao',
        )

        self.product_bad = Product.objects.create(
            name='Nutella',
            code='',
            nutri_score='E',
            link='https://fr.openfoodfacts.org/produit/80762003/nutella-ferrero',
            quantity='400 G',
            image='https://static.openfoodfacts.org/images/products/80762003/front_fr.3.400.jpg',
            category=self.category,
            nutriment_energy='2252',
            nutriment_sugars='56.3',
            nutriment_salt='0.107',
            nutriment_fat='30.9',
            nutriment_saturated_fat='10.6',
            nutriment_sodium='0.0428',
            nutriment_proteins='6.3',
            nutriment_carbohydrates='57.5',
            nutriment_fiber='7',
        )

        self.product_good = Product.objects.create(
            name='Tartimouss noisette cacao et lait',
            code='3770012968304',
            nutri_score='B',
            link='https://static.openfoodfacts.org/images/products/377/001/296/8304/front_fr.3.400.jpg',
            quantity='220 G',
            image='https://static.openfoodfacts.org/images/products/377/001/296/8304/front_fr.3.400.jpg',
            category=self.category,
            nutriment_energy='1251',
            nutriment_sugars='34',
            nutriment_salt='0.21',
            nutriment_fat='9.9',
            nutriment_saturated_fat='0.9',
            nutriment_sodium='0.084',
            nutriment_proteins='8.9',
            nutriment_carbohydrates='41',
            nutriment_fiber='5.8',
        )

    def test_product_substitute_add(self):
        product_substitute = ProductSubstitute.objects.create(
            product=self.product_bad,
            substitute_product=self.product_good,
            user=self.user,
        )
        self.assertEqual(ProductSubstitute.objects.first(), product_substitute)

    def test_product_substitute_str(self):
        for product_substitute in ProductSubstitute.objects.all():
            self.assertEqual(product_substitute.__str__(), product_substitute.name)

    def test_product_substitute_delete_all(self):
        ProductSubstitute.objects.all().delete()
        self.assertEqual(len(ProductSubstitute.objects.all()), 0)
