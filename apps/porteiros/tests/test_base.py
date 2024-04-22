from porteiros.models import Porteiro
from usuarios.models import Usuario
from visitantes.models import Visitante

from django.test import TestCase


class BaseTest(TestCase):
    def make_usuario(self):
        usuario = Usuario.objects.create(
            email='testuser@email.com',
            password='123456'
        )
        usuario.save()
        return usuario

    def make_porteiro(self):
        usuario = self.make_usuario()
        return Porteiro(
            usuario=usuario,
            nome_completo='Porteiro Test',
            cpf='11122234576',
            telefone='991559553',
            data_nascimento='1993-03-21',
        )

    def make_visitante(self):
        porteiro = self.make_porteiro()
        return Visitante(
            status='AGUARDANDO',
            nome_completo='Visitante test',
            cpf='11133322256',
            data_nascimento='1995-05-25',
            numero_casa='100',
            registrado_por=porteiro,
        )
