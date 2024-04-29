from visitantes.views import site
from porteiros.tests.test_base import BaseTest

from django.urls import reverse, resolve
from django.utils import timezone


class VisitantesFinalizarVisitaViewTest(BaseTest):

    def test_visitantes_finalizar_visita_view_function_is_correct(self):
        view = resolve(reverse('finalizar_visita', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, site.FinalizarVisitaView)

    def test_visitantes_finalizar_visita_view_function_return_405_if_method_get(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('finalizar_visita', kwargs={'id': visitante.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 405)

    def test_visitantes_finalizar_visita_view_function_return_405_if_method_patch(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('finalizar_visita', kwargs={'id': visitante.id})
        response = self.client.patch(url)

        self.assertEqual(response.status_code, 405)

    def test_visitantes_finalizar_visita_view_function_return_405_if_method_put(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('finalizar_visita', kwargs={'id': visitante.id})
        response = self.client.put(url)

        self.assertEqual(response.status_code, 405)

    def test_visitantes_finalizar_visita_view_function_return_405_if_method_delete(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('finalizar_visita', kwargs={'id': visitante.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 405)

    def test_visitantes_finalizar_visita_view_function_will_redirect_without_auth_user_status_code_302(self):  # noqa: E501
        url = reverse('finalizar_visita', kwargs={'id': 1})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_visitantes_finalizar_visita_view_with_auth_user_dont_find_visitante_return_404(self):  # noqa: E501
        visitante = self.make_visitante()
        fake_id = visitante.id + 9999999999

        url = reverse('finalizar_visita', kwargs={'id': fake_id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)

    def test_visitantes_finalizar_visita_view_with_auth_user_finaliza_a_visita(self):  # noqa: E501
        hoje = timezone.now()

        visitante = self.make_visitante()

        url = reverse('finalizar_visita', kwargs={'id': visitante.id})
        response = self.client.post(url, follow=True)

        visitante.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(visitante.status, 'FINALIZADO')
        self.assertEqual(visitante.horario_saida.date(), hoje.date())
        self.assertContains(response, "Visita finalizada com sucesso")
        self.assertRedirects(response, reverse('index'))
