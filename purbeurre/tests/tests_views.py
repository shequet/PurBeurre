from django.test import TestCase
from django.contrib.auth.models import User
from purbeurre.models import Product, Category, ProductSubstitute


class TestLegalIndexView(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contain_view(self):
        response = self.client.get('/')
        self.assertContains(response, 'Colette et Remy')


class TestLegalMentionsView(TestCase):
    def test_legal_mentions_view(self):
        response = self.client.get('/legal_mentions/')
        self.assertEqual(response.status_code, 200)

    def test_legal_contain_view(self):
        response = self.client.get('/legal_mentions/')
        self.assertContains(response, 'Mentions Légales Site Internet')


class TestLegalContactView(TestCase):
    def test_contact_view(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_contain_view(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'contact@purbeurre.fr')


class TestProductView(TestCase):

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
            eco_score='D',
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
            eco_score='C',
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

    def test_product_substitute_user_connected_view(self):
        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.get('/product_substitute/')
        self.assertEqual(response.status_code, 200)

    def test_product_substitute_not_connected_view(self):
        response = self.client.get('/product_substitute/')
        self.assertEqual(response.status_code, 302)

    def test_product_search(self):
        response = self.client.post('/product/search/', {
            'name': 'nutella'
        })
        self.assertEqual(response.status_code, 200)

    def test_product_search_contain_view(self):
        response = self.client.post('/product/search/', {
            'name': 'nutella'
        })
        self.assertContains(response, 'nutella')

    def test_product_detail(self):
        response = self.client.post('/product/{product_id}/'.format(
            product_id=self.product_good.id
        ))
        self.assertEqual(response.status_code, 200)

    def test_product_contain_detail(self):
        response = self.client.post('/product/{product_id}/'.format(
            product_id=self.product_good.id
        ))
        self.assertContains(response, self.product_good.link)

    def test_product_substitute_add(self):
        self.client.login(
            username=self.username,
            password=self.password
        )

        response = self.client.get('/product_substitute/{product_id}/{substitute_product_id}/add/'.format(
            product_id=self.product_bad.id,
            substitute_product_id=self.product_good.id
        ))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ProductSubstitute.objects.filter(user=self.user).count(), 1)

    def test_product_substitute_delete(self):
        self.client.login(
            username=self.username,
            password=self.password
        )

        response = self.client.get('/product_substitute/{product_id}/{substitute_product_id}/delete/'.format(
            product_id=self.product_bad.id,
            substitute_product_id=self.product_good.id
        ))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ProductSubstitute.objects.filter(user=self.user).count(), 0)
