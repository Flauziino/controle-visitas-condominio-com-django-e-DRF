from django.test import TestCase
from django.urls import reverse


class DashboardURLsTest(TestCase):

    # teste de URLS
    def test_dashboard_index_url_is_correct(self):
        url = reverse('index')
        self.assertEqual(url, '/')
