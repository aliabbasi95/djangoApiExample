from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AccountsTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        self.register_url = reverse('account_register')

    def test_register_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'Somepassword1@'
        }

        response = self.client.post(self.register_url, data, format='json')  # new

        # We want to make sure we have two users in the database.
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_register_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 12.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': 'f@2F'
        }

        response = self.client.post(self.register_url, data, format='json')
        # We want to make sure we have one user in the database.
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 400 created code.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # And check length of password in response data equal 1
        self.assertEqual(len(response.data['password']), 1)

    def test_register_user_with_no_password(self):
        """
        Ensure user is not created for no password.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': ''
        }

        response = self.client.post(self.register_url, data, format='json')
        # We want to make sure we have one user in the database.
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 400 created code.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # And check password in response data equal 1
        self.assertEqual(len(response.data['password']), 1)

    def test_register_user_with_password_has_not_number(self):
        """
        Ensure user is not created for password has not numbered.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': 'TestPassword@'
        }

        response = self.client.post(self.register_url, data, format='json')
        # We want to make sure we have one user in the database..
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 400 created code.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # And check password in response data equal 1
        self.assertEqual(len(response.data['password']), 1)

    def test_register_user_with_password_has_not_upper(self):
        """
        Ensure user is not created for password has not upper.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': 'testpassword1@'
        }

        response = self.client.post(self.register_url, data, format='json')
        # We want to make sure we have one user in the database..
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 400 created code.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # And check password in response data equal 1
        self.assertEqual(len(response.data['password']), 1)
