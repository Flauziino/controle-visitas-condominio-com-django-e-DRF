from django.urls import reverse

from rest_framework import serializers

from parameterized import parameterized

from visitantes.models import Visitante
from visitantes.tests.test_visitantes_api_base import APIBaseTestMixin


class TestAPISerializers(APIBaseTestMixin):
    # //////////////////////////
    # TESTES VISITANTESERIALIZER
    def test_serializer_registrar_visitante_fail_cus_nome_completo_length_lt_5_status_code_400_bad_request(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test",
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
        # checa inicialmente se recebeu um bad request (code 400)
        self.assertEqual(
            response.status_code, 400
        )

    def test_serializer_registrar_visitante_fail_cus_nome_completo_length_lt_5_raises_validation_error(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # checa se deu raise no error do serializer
        self.assertRaises(serializers.ValidationError)

    def test_serializer_registrar_visitante_fail_cus_nome_completo_length_lt_5_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test",
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
        # checa se a msg de erros estao contidas no serializer
        self.assertContains(
            response,
            'Por favor, digite o nome completo do visitante',
            status_code=400
        )

    def test_serializer_registrar_visitante_fail_cus_cpf_length_different_than_11_status_code_400_bad_request(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "1112223334",
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
        # checa inicialmente se recebeu um bad request (code 400)
        self.assertEqual(
            response.status_code, 400
        )

    def test_serializer_registrar_visitante_fail_cus_cpf_length_different_than_11_raises_validation_error(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "1112223334",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # checa se deu raise no error do serializer
        self.assertRaises(serializers.ValidationError)

    def test_serializer_registrar_visitante_fail_cus_cpf_length_different_than_11_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "1112223334",
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
        # checa se a msg de erros estao contidas no serializer
        self.assertContains(
            response,
            'Por favor, digite um cpf válido (11 digitos)',
            status_code=400
        )

    def test_serializer_registrar_visitante_fail_cus_numero_casa_cant_be_empty_or_none_status_code_400_bad_request(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "11122233347",
            "data_nascimento": "1995-12-12",
            "numero_casa": ""
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # checa inicialmente se recebeu um bad request (code 400)
        self.assertEqual(
            response.status_code, 400
        )

    def test_serializer_registrar_visitante_fail_cus_numero_casa_cant_be_empty_or_none_raises_validation_error(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "11122233347",
            "data_nascimento": "1995-12-12",
            "numero_casa": ""
        }

        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # checa se deu raise no error do serializer
        self.assertRaises(serializers.ValidationError)

    def test_serializer_registrar_visitante_fail_cus_numero_casa_cant_be_empty_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "11122233347",
            "data_nascimento": "1995-12-12",
            "numero_casa": ""
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        self.assertContains(
            response,
            "Este campo não pode ser em branco.",
            status_code=400
        )

    def test_serializer_registrar_visitante_fail_cus_numero_casa_cant_be_none_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test serializer",
            "cpf": "11122233347",
            "data_nascimento": "1995-12-12",
            "numero_casa": None
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        self.assertContains(
            response,
            "Este campo não pode ser nulo.",
            status_code=400
        )

    @parameterized.expand([
        ('nome_completo', "Este campo não pode ser em branco."),
        ('cpf', "Este campo não pode ser em branco."),
        ('data_nascimento', "Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD."),  # noqa: E501
    ])
    def test_serializers_fields_cant_be_empty_checks_message(self, field, msg):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            field: "",
            field: "",
            field: "",
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        self.assertContains(
            response,
            msg,
            status_code=400
        )

    @parameterized.expand([
        ('nome_completo', "Este campo não pode ser nulo."),
        ('cpf', "Este campo não pode ser nulo."),
        ('data_nascimento', "Este campo não pode ser nulo."),
    ])
    def test_serializers_fields_cant_be_none_checks_message(self, field, msg):
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            field: None,
            field: None,
            field: None
        }

        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        self.assertContains(
            response,
            msg,
            status_code=400
        )

    # ////////////////////////////////
    # TEST AUTORIZAVISITANTESERIALIZER
    def test_serializer_informacoes_visitante_fail_cus_morador_responsavel_cant_be_empty_or_none_status_code_400_bad_request(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test completo",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        # criando visitante
        api_url = reverse('registrar_visitante_api')
        response = self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # buscando visitante criado no banco de dados
        visitante = Visitante.objects.all().first()

        # dados para autorizar visitante
        data_autoriza = {
            "morador_responsavel": ""
        }

        # tentando autorizar o visitante com o campo em branco
        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            data=data_autoriza,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )
        # checa inicialmente se recebeu um bad request (code 400)
        self.assertEqual(
            response.status_code, 400
        )

    def test_serializer_informacoes_visitante_fail_cus_morador_responsavel_cant_be_empty_or_none_raises_validation_error(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test completo",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        # criando visitante
        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # buscando visitante criado no banco de dados
        visitante = Visitante.objects.all().first()

        # dados para autorizar visitante
        data_autoriza = {
            "morador_responsavel": ""
        }

        # tentando autorizar o visitante com o campo em branco
        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        self.client.post(
            api_url,
            data=data_autoriza,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )
        # checa se deu raise no error do serializer
        self.assertRaises(serializers.ValidationError)

    def test_serializer_informacoes_visitante_fail_cus_morador_responsavel_cant_be_empty_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test completo",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        # criando visitante
        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # buscando visitante criado no banco de dados
        visitante = Visitante.objects.all().first()

        # dados para autorizar visitante
        data_autoriza = {
            "morador_responsavel": ""
        }

        # tentando autorizar o visitante com o campo em branco
        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            data=data_autoriza,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )
        # checa se a msg de erros estao contidas no serializer
        self.assertContains(
            response,
            "Este campo não pode ser em branco.",
            status_code=400
        )

    def test_serializer_informacoes_visitante_fail_cus_morador_responsavel_cant_be_none_checks_message(self):  # noqa: E501
        auth_data = self.get_auth_data()
        jwt_access = auth_data.get('jwt_access_token')

        # dados para criar visitante com a API
        data = {
            "nome_completo": "test completo",
            "cpf": "11122233345",
            "data_nascimento": "1995-12-12",
            "numero_casa": "97"
        }

        # criando visitante
        api_url = reverse('registrar_visitante_api')
        self.client.post(
            api_url,
            data=data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}',

        )
        # buscando visitante criado no banco de dados
        visitante = Visitante.objects.all().first()

        # dados para autorizar visitante
        data_autoriza = {
            "morador_responsavel": None
        }

        # tentando autorizar o visitante com o campo None
        api_url = reverse(
            'informacoes_visitante_api',
            kwargs={'id': visitante.id}
        )
        response = self.client.post(
            api_url,
            data=data_autoriza,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )
        # checa se a msg de erros estao contidas no serializer
        self.assertContains(
            response,
            "Este campo não pode ser nulo.",
            status_code=400
        )
