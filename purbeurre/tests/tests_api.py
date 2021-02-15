from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from purbeurre.openfoodfact import OpenFoodFacts


class TestOpenFoodFact(TestCase):
    def setUp(self) -> None:
        self.openfoodfact = OpenFoodFacts()
        self.products = []

    def test_call_category(self):
        self.products = self.openfoodfact.get_category('pates-a-tartiner-aux-noisettes-et-au-cacao')
        self.assertTrue(700 <= len(self.products))

    def test_decode_nutriscore(self):
        for product in self.products:
            self.assertIsNotNone(self.openfoodfact.decode_nutriscore(product.nutri_score))


class CommandImport(TestCase):
    def command_import(self, *args, **kwargs):
        return call_command(
            'import',
            *args,
            stdout=StringIO(),
            stderr=StringIO(),
            **kwargs,
        )

    def test_command_import(self):
        output = self.command_import('pates-a-tartiner-aux-noisettes-et-au-cacao')
        self.assertNotIn(output, ['Error'])

