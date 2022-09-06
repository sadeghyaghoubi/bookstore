from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
##barresi khode URL : agar to url aslie proje esmesh taghir kone in khata mide
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

##agar esme url taghir kone inja khata mide
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_Title(self):
        response = self.client.get(reverse('home'))
        self.assertContains (response, 'Home Page')

    def Home_Page_Template_Used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
