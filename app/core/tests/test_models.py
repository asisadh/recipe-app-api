from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@email.com'
        password = 'Nepal123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test the new email for new user is normalised"""
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, 'Nepal123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Nepal123')

    def test_create_new_super_user(self):
        """Test create a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@super.user',
            'Nepal123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
