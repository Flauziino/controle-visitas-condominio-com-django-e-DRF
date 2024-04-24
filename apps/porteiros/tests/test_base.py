from porteiros.models import Porteiro
from usuarios.models import Usuario
from visitantes.models import Visitante

from django.test import TestCase
from django.utils import timezone


class BaseTest(TestCase):
    def make_usuario(self):
        usuario = Usuario.objects.create(
            email='testuser@email.com',
            password='123456'
        )
        self.client.force_login(usuario)
        usuario.save()
        return usuario

    def make_porteiro(self):
        usuario = self.make_usuario()
        usuario.save()
        porteiro = Porteiro(
            usuario=usuario,
            nome_completo='Porteiro Test',
            cpf='11122234576',
            telefone='991559553',
            data_nascimento='1993-03-21',
        )
        porteiro.save()
        return porteiro

    def make_visitante(self):
        hoje = timezone.now().date()
        porteiro = self.make_porteiro()
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
        return visitante

    def make_visitante_with_no_default(self):
        porteiro = self.make_porteiro()
        return Visitante(
            nome_completo='Visitante test',
            cpf='11133322256',
            data_nascimento='1995-05-25',
            numero_casa='100',
            registrado_por=porteiro,
        )
