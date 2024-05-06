from django.utils import timezone
from django.urls import reverse, resolve

from visitantes.views import api
from visitantes.models import Visitante
from visitantes.tests.test_visitantes_api_base import APIBaseTestMixin


class TestFinalizarVisitaAPIView(APIBaseTestMixin):

    def test_finalizar_visita_api_view_function_is_correct(self):
        view = resolve(
            reverse('finalizar_visita_api', kwargs={'id': 1})
        )

        self.assertIs(view.func.view_class, api.FinalizaVisitaAPIView)

    def test_finalizar_visita_api_view_without_auth_user_return_401(self):
        api_url = reverse('finalizar_visita_api', kwargs={'id': 1})
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, 401)

    def test_finalizar_visita_api_view_with_auth_user_return_405_if_method_get(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('finalizar_visita_api', kwargs={'id': 1})
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_finalizar_visita_api_view_with_auth_user_return_405_if_method_patch(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('finalizar_visita_api', kwargs={'id': 1})
        response = self.client.patch(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_finalizar_visita_api_view_with_auth_user_return_405_if_method_put(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('finalizar_visita_api', kwargs={'id': 1})
        response = self.client.put(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_finalizar_visita_api_view_with_auth_user_return_405_if_method_delete(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('finalizar_visita_api', kwargs={'id': 1})
        response = self.client.delete(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_finalizar_visita_api_view_with_auth_user_return_404_if_dont_find_visitante(self):  # noqa: E501
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
            'finalizar_visita_api',
            kwargs={'id': fake_id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        # verificando se recebeu o codigo 404 e tudo esta correto.
        self.assertEqual(response.status_code, 404)

    def test_finalizar_visita_api_view_with_auth_user_return_status_code_200(self):  # noqa: E501
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
            'finalizar_visita_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        # verificando se recebeu o codigo 200 e tudo esta correto.
        self.assertEqual(response.status_code, 200)

    def test_finalizar_visita_api_view_with_auth_user_change_visitante_status(self):  # noqa: E501
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
            'finalizar_visita_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        visitante.refresh_from_db()
        # verificando se o status foi alterado corretamente no db
        self.assertEqual(visitante.status, 'FINALIZADO')

    def test_finalizar_visita_api_view_with_auth_user_horario_saida_is_correct(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # pegando a hora atual para comparativo futuro.
        agora = timezone.now()

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
            'finalizar_visita_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        visitante.refresh_from_db()
        # verificando se as datas de saida estao corretas
        self.assertEqual(visitante.horario_saida.date(), agora.date())

    def test_finalizar_visita_api_view_with_auth_user_returns_correct_message(self):  # noqa: E501
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
            'finalizar_visita_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        visitante.refresh_from_db()
        # verificando se 'message' esta na response.data
        self.assertIn('message', response.data)
        # verificando se a message é a mesma que a esperada
        self.assertIn(
            f'Visita de {visitante.nome_completo} finalizada',
            response.data['message']
        )
