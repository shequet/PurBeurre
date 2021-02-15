from django.test import TestCase
from django.contrib.auth.models import User


class UserModel(TestCase):

    def test_user_add(self):
        email = 'test@gmail.com'
        password = 'password'

        User.objects.create_user(
            username=email,
            password=password
        )

        user = User.objects.first()
        self.assertEqual(user, user)

    def test_user_delete_all(self):
        User.objects.all().delete()
        self.assertEqual(len(User.objects.all()), 0)
