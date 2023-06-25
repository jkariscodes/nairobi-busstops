from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import WebMapView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        self.assertTemplateUsed(self.response, "webmap.html")

    def test_html_content(self):
        self.assertNotContains(self.response, "I hate maps!")

    def test_url_resolve_home(self):
        home_view = resolve("/")
        self.assertEqual(home_view.func.__name__, WebMapView.as_view().__name__)
