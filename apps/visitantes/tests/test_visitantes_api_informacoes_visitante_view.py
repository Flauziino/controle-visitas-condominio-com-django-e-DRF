from django.urls import reverse, resolve

from visitantes.views import api
from visitantes.models import Visitante
from visitantes.tests.test_visitantes_api_base import APIBaseTestMixin


class TestInformacoesVisitanteAPIView(APIBaseTestMixin):

    def test_informacoes_visitante_api_view_function_is_correct(self):
        view = resolve(
            reverse('informacoes_visitante_api', kwargs={'id': 1})
        )

        self.assertIs(view.func.view_class, api.InformacoesVisitanteAPIView)

    def test_informacoes_visitante_api_view_without_auth_user_return_401(self):
        api_url = reverse('informacoes_visitante_api', kwargs={'id': 1})
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, 401)

    def test_informacoes_visitante_api_view_with_auth_user_return_200_if_find_visitante(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        # verificando se recebeu o codigo 200 e tudo esta correto.
        self.assertEqual(response.status_code, 200)
        # verificando se foi retornado o data correto
        self.assertIn("nome_pagina", response.data)
        self.assertIn("visitante", response.data)

    def test_informacoes_visitante_api_view_with_auth_user_return_404_if_dont_find_visitante_method_get(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()
        # simulando um ID falso para que nao se encontre o visitante
        fake_id = visitante.id + 99999999999

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': fake_id}
        )
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        # verificando se recebeu o codigo 404 e tudo esta correto.
        self.assertEqual(response.status_code, 404)

    def test_informacoes_visitante_api_view_with_auth_user_return_405_if_method_patch(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        # verificando a response com method patch
        response = self.client.patch(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_informacoes_visitante_api_view_with_auth_user_return_405_if_method_put(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        # verificando a response com method put
        response = self.client.put(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_informacoes_visitante_api_view_with_auth_user_return_405_if_method_delete(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        # verificando a response com method delete
        response = self.client.delete(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_informacoes_visitante_api_view_with_auth_user_return_404_if_dont_find_visitante_method_post(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()
        # simulando um ID falso para que nao se encontre o visitante
        fake_id = visitante.id + 99999999999

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': fake_id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        # verificando se recebeu o codigo 404 e tudo esta correto.
        self.assertEqual(response.status_code, 404)

    def test_informacoes_visitante_api_view_with_auth_user_find_visitand_but_got_invalid_data_return_400(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 400)

    def test_informacoes_visitante_api_view_with_auth_user_find_visitante_and_receive_valid_data(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test visitante",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # conferindo se foi recebido code 201 (created)
        self.assertEqual(response.status_code, 201)

        # buscando visitante no banco de dados
        visitante = Visitante.objects.all().first()

        data = {
            'morador_responsavel': 'morador test'
        }

        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 200)
        # verificando se a msg de sucesso esta na resposta
        self.assertIn(
            f'Visitante {visitante.nome_completo} autorizado',
            response.data['message']
        )
