from django.utils import timezone
from django.urls import reverse, resolve

from visitantes.views import api
from visitantes.models import Visitante
from visitantes.tests.test_visitantes_api_base import APIBaseTestMixin


class TestIndexAPIView(APIBaseTestMixin):

    def test_index_api_view_function_is_correct(self):
        view = resolve(
            reverse('index_api')
        )

        self.assertIs(view.func.view_class, api.IndexAPIView)

    def test_index_api_view_function_will_be_unauthorized_without_auth_user(self):  # noqa: E501
        url = reverse('index_api')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)

    def test_index_api_view_funcition_with_auth_user_return_status_code_200(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 200)

    def test_index_api_view_will_receive_status_code_405_if_method_post(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_index_api_view_will_receive_status_code_405_if_method_patch(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.patch(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_index_api_view_will_receive_status_code_405_if_method_put(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.put(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_index_api_view_will_receive_status_code_405_if_method_delete(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.delete(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_index_api_returns_nome_pagina_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('nome_pagina', response.data)

    def test_index_api_returns_todos_visitantes_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('todos_visitantes', response.data)

    def test_index_api_returns_visitantes_aguardando_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('visitantes_aguardando', response.data)

    def test_index_api_returns_visitantes_em_visita_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('visitantes_em_visita', response.data)

    def test_index_api_returns_visitantes_finalizado_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('visitantes_finalizado', response.data)

    def test_index_api_returns_visitante_mes_in_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertIn('visitante_mes', response.data)

    def test_index_api_correct_logic_of_dashboard(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        hoje = timezone.now().date()

        porteiro = auth_data.get('porteiro')
        visitante = Visitante(
            status='AGUARDANDO',
            nome_completo='Visitante test',
            cpf='11133322256',
            data_nascimento='1995-05-25',
            numero_casa='100',
            horario_chegada=hoje,
            registrado_por=porteiro,
        )
        visitante.save()

        api_url = reverse('index_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        visitante_aguardando = response.data['visitantes_aguardando']

        self.assertEqual(visitante_aguardando, 1)
