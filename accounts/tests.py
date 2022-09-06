from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpPageTest(TestCase):
    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_Title(self):
        response = self.client.get(reverse('signup'))
        self.assertContains (response, 'Sign Up')

    user_name = 'myusername'
    email = 'myusername@gmail.com'
    def test_signup_forms(self):
        user = get_user_model().objects.create_user(
            self.user_name,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'myusername')
        self.assertEqual(get_user_model().objects.all()[0].email, 'myusername@gmail.com')