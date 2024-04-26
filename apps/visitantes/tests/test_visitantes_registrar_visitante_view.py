from visitantes import views
from porteiros.tests.test_base import BaseTest

from django.urls import reverse, resolve


class VisitantesRegistrarVisitanteViewTest(BaseTest):

    def test_visitantes_registrar_visitantes_view_function_is_correct(self):
        view = resolve(reverse('registrar_visitante'))
        self.assertIs(view.func.view_class, views.RegistrarVisitanteView)

    def test_visitantes_registrar_visitantes_view_will_redirect_if_not_auth_status_code_302_get_method(self):  # noqa: E501
        url = reverse('registrar_visitante')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_visitantes_registrar_visitantes_view_will_redirect_if_not_auth_status_code_302_post_method(self):  # noqa: E501
        url = reverse('registrar_visitante')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_visitantes_registrar_visitantes_view_with_auth_user_status_code_200_get_method(self):  # noqa: E501
        self.make_porteiro()

        url = reverse('registrar_visitante')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_visitantes_registrar_visitantes_view_with_auth_user_status_code_200_post_method(self):  # noqa: E501
        self.make_porteiro()

        url = reverse('registrar_visitante')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)

    def test_visitantes_registrar_visitantes_view_with_auth_user_use_the_right_template_with_get_method(self):  # noqa: E501
        self.make_porteiro()

        url = reverse('registrar_visitante')
        response = self.client.get(url)

        self.assertTemplateUsed(response, "registrar_visitante.html")

    def test_visitantes_registrar_visitantes_view_with_auth_user_context(self):
        self.make_porteiro()

        url = reverse('registrar_visitante')
        response = self.client.get(url)

        self.assertIn('nome_pagina', response.context)
        self.assertIn('form', response.context)

    def test_visitantes_registrar_visitantes_view_with_auth_user_Registrar_visitante_in_context(self):  # noqa: E501
        self.make_porteiro()

        url = reverse('registrar_visitante')
        response = self.client.get(url)

        self.assertIn(
            "Registrar visitante",
            response.context['nome_pagina']
        )

    def test_visitantes_registrar_visitantes_receive_valid_form_and_create_visitante(self):  # noqa: E501
        self.make_porteiro()

        form_data = {
            "nome_completo": 'Test',
            "cpf": '11133322245',
            "data_nascimento": '1993-05-15',
            "numero_casa": '100',
            "placa_veiculo": '1234567'
        }

        url = reverse('registrar_visitante')
        response = self.client.post(url, data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))
        self.assertContains(
            response,
            "Visitante registrado com sucesso!"
        )
