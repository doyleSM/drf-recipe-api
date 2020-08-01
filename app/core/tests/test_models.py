from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="teste@gmail.com", password="testepass"):
    """"create a sample_user"""
    return get_user_model().objects.create(email=email, password=password)


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating new user with email is succesfull"""
        email = 'test@gmail.com'
        password = '123456ASDFGH'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """teste the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'teste123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234567')

    def test_create_new_super_user(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'teste@gmail.com',
            '123456'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag string representional"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Barbecue"
        )

        self.assertEqual(str(tag), tag.name)