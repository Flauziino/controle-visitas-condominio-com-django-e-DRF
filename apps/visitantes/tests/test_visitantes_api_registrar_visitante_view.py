from django.urls import reverse, resolve

from visitantes.views import api
from visitantes.tests.test_visitantes_api_base import APIBaseTestMixin


class TestRegistrarVisitanteAPIView(APIBaseTestMixin):

    def test_registrar_visitante_api_view_function_is_correct(self):
        view = resolve(
            reverse('registrar_visitante_api')
        )

        self.assertIs(view.func.view_class, api.RegistrarVisitanteAPIView)

    def test_registrar_visitante_api_view_function_will_return_401_without_auth_user(self):  # noqa: E501
        api_url = reverse('registrar_visitante_api')
        response = self.client.post(api_url)

        self.assertEqual(response.status_code, 401)

    def test_registrar_visitante_api_view_funcition_with_auth_user_return_status_code_400_without_or_invalid_data(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 400)

    def test_registrar_visitante_api_view_will_receive_status_code_405_if_method_get(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('registrar_visitante_api')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_registrar_visitante_api_view_will_receive_status_code_405_if_method_put(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('registrar_visitante_api')
        response = self.client.put(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_registrar_visitante_api_view_will_receive_status_code_405_if_method_patch(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('registrar_visitante_api')
        response = self.client.patch(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_registrar_visitante_api_view_will_receive_status_code_405_if_method_delete(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        api_url = reverse('registrar_visitante_api')
        response = self.client.delete(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

        self.assertEqual(response.status_code, 405)

    def test_registrar_visitante_api_create_visitante_with_valid_data(self):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

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

        self.assertEqual(response.status_code, 201)
