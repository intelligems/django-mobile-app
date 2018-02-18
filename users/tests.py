from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Account


class APITests(TestCase):
    def setUp(self):
        self.account = Account.objects.create_user(
            username="test",
            password="test1234"
        )

    def test_auth(self):
        """
        Ensure we can successfully get authorized via the API
        """
        request = self.client.post(
            reverse('rest_login'),
            {'username': 'test', 'password': 'test1234'}
        )
        self.assertEqual(request.status_code, 200)

    def test_account_me_unauthorized(self):
        """
        Ensure the `me` accounts endpoint does to return data to unauthorized requests
        """
        client = APIClient()
        # client.login(username='test', password='test1234')
        request = client.get(reverse('api_accounts_me'))
        self.assertEqual(request.status_code, 401)

    def test_account_me_authorized(self):
        """
        Ensure the `me` accounts endpoint returns the correct data to authorized requests
        """
        token = Token.objects.get(user=self.account)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.get(reverse('api_accounts_me'))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data.get('id'), self.account.id)

    def test_account_update(self):
        """
        Ensure our update requests get executed correctly
        """
        token = Token.objects.get(user=self.account)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.patch(reverse('api_accounts_me'), data={'first_name': 'FirstName'})
        self.assertEqual(request.status_code, 200)
        request2 = client.get(reverse('api_accounts_me'))
        self.assertEqual(request2.data.get('first_name'), 'FirstName')
