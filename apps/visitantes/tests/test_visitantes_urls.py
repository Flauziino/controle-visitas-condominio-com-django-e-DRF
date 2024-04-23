from django.test import TestCase
from django.urls import reverse


class VisitantesURLsTest(TestCase):

    # teste de URLS
    def test_visitantes_registrar_visitante_url_is_correct(self):
        url = reverse('registrar_visitante')
        self.assertEqual(url, '/registrar-visitante/')

    def test_visitantes_informacoes_visitante_url_is_correct(self):
        url = reverse('informacoes_visitante', kwargs={'id': 1})
        self.assertEqual(url, '/visitantes/1')

    def test_visitantes_finalizar_visita_url_is_correct(self):
        url = reverse('finalizar_visita', kwargs={'id': 1})
        self.assertEqual(url, '/visitantes/1/finalizar-visita')
