from rest_framework import test

from django.urls import reverse

from usuarios.models import Usuario
from porteiros.models import Porteiro
from porteiros.tests.test_base import BaseTest


class APIBaseTestMixin(test.APITestCase, BaseTest):
    def get_auth_data(self):
        usuario = Usuario.objects.create_user(
            email='testuser@email.com',
            password='123456'
        )
        usuario.save()

        data = {
            'email': usuario.email,
            'password': '123456'
        }

        porteiro = Porteiro(
            usuario=usuario,
            nome_completo='Porteiro Test',
            cpf='11122234576',
            telefone='991559553',
            data_nascimento='1993-03-21',
        )
        porteiro.save()

        response = self.client.post(
            reverse('token_obtain_pair'), data={**data}
        )
        return {
            'jwt_access_token': response.data.get('access'),
            'jwt_refresh_token': response.data.get('refresh'),
            'porteiro': porteiro,
            'data': data
        }
