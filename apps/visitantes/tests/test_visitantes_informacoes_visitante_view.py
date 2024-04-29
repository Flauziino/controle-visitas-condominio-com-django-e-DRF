from visitantes.views import site
from porteiros.tests.test_base import BaseTest

from django.urls import reverse, resolve
from django.utils import timezone


class VisitantesInformacoesVisitanteViewTest(BaseTest):

    def test_visitantes_informacoes_visitante_view_function_is_correct(self):
        view = resolve(reverse('informacoes_visitante', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, site.InformacoesVisitante)

    def test_visitantes_informacoes_visitante_view_will_redirect_if_not_auth_status_code_302_get_method(self):  # noqa: E501
        url = reverse('informacoes_visitante', kwargs={'id': 1})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_visitantes_informacoes_visitante_view_will_redirect_if_not_auth_status_code_302_post_method(self):  # noqa: E501
        url = reverse('informacoes_visitante', kwargs={'id': 1})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_visitantes_informacoes_visitante_view_with_auth_user_status_code_200_get_method_if_have_visitante(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('informacoes_visitante', kwargs={'id': visitante.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_visitantes_informacoes_visitante_view_with_auth_user_status_code_404_if_dont_find_visitante(self):  # noqa: E501
        visitante = self.make_visitante()
        fake_id = visitante.id + 9999

        url = reverse('informacoes_visitante', kwargs={'id': fake_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_visitantes_informacoes_visitante_view_with_auth_user_use_the_right_template_with_get_method(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('informacoes_visitante', kwargs={'id': visitante.id})
        response = self.client.get(url)

        self.assertTemplateUsed(response, "informacoes_visitante.html")

    def test_visitantes_informacoes_visitante_view_with_auth_user_context(self):  # noqa: E501
        visitante = self.make_visitante()

        url = reverse('informacoes_visitante', kwargs={'id': visitante.id})
        response = self.client.get(url)

        self.assertIn('nome_pagina', response.context)
        self.assertIn('visitante', response.context)
        self.assertIn('form', response.context)

    def test_visitantes_informacoes_visitante_view_with_auth_user_and_post_method_with_valid_form_confirm_visitante(self):  # noqa: E501
        hoje = timezone.now().date()

        visitante = self.make_visitante()

        autoriza_data = {
            'morador_responsavel': 'test_autoriza'
        }

        url = reverse('informacoes_visitante', kwargs={'id': visitante.id})
        response = self.client.post(url, data=autoriza_data, follow=True)

        visitante.refresh_from_db()
        self.assertEqual(visitante.status, 'EM_VISITA')
        self.assertEqual(visitante.horario_autorizacao.date(), hoje)
        self.assertIn(
            "Entrada de visitante autorizada com sucesso",
            response.content.decode('utf-8')
        )
        self.assertRedirects(response, reverse('index'))

    def test_visitantes_informacoes_visitante_view_with_auth_user_and_post_method_with_invalid_form_confirm_visitante(self):  # noqa: E50
        visitante = self.make_visitante()

        autoriza_data = {
            'morador_responsavel': ''
        }

        url = reverse('informacoes_visitante', kwargs={'id': visitante.id})
        response = self.client.post(url, data=autoriza_data)

        self.assertEqual(response.status_code, 200)
