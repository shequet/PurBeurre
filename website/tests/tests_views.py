from django.test import Client, TestCase


class TestAccountView(TestCase):

    def setUp(self):
        self.username = 'test@gmail.com'
        self.password = 'password1AB'

    def test_account_register(self):
        csrf_client = Client(enforce_csrf_checks=False)
        response = csrf_client.post('/accounts/register/', {
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })

        self.assertEqual(response.status_code, 302)

    def test_account_login(self):
        csrf_client = Client(enforce_csrf_checks=False)
        response = csrf_client.post('/accounts/login/', {
            'username': self.username,
            'password': self.password,
        })

        self.assertEqual(response.status_code, 200)

    def test_account_profile(self):
        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.get('/accounts/profile/')

        self.assertEqual(response.status_code, 302)

