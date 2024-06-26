from dashboard import views
from porteiros.tests.test_base import BaseTest

from django.urls import reverse, resolve


class DashboardIndexViewTest(BaseTest):
    def test_dashboard_index_view_function_is_correct(self):
        view = resolve(reverse('index'))
        self.assertIs(view.func.view_class, views.IndexView)

    def test_dashboard_index_view_redirect_if_not_auth_user_status_code_302(self):  # noqa : E501
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_index_view_status_code_200_if_auth_user(self):
        # criando usuario
        user = self.make_usuario()
        # autenticando usuario
        self.client.force_login(user)

        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_view_uses_correct_template(self):
        # criando usuario
        user = self.make_usuario()
        # autenticando usuario
        self.client.force_login(user)

        url = reverse('index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')

    def test_dashboard_index_view_context_is_ok(self):
        # criando usuario
        user = self.make_usuario()
        # autenticando usuario
        self.client.force_login(user)

        url = reverse('index')
        response = self.client.get(url)
        # verificando todos itens do contexto
        self.assertIn("nome_pagina", response.context)
        self.assertIn('todos_visitantes', response.context)
        self.assertIn('visitantes_aguardando', response.context)
        self.assertIn('visitantes_em_visita', response.context)
        self.assertIn('visitantes_finalizado', response.context)
        self.assertIn('visitante_mes', response.context)

    def test_dashboard_index_view_status_is_aguardando(self):
        # criando visitante para teste
        visitante = self.make_visitante()
        # extraindo o usuario para realizar o login
        porteiro = visitante.registrado_por
        user = porteiro.usuario
        self.client.force_login(user)

        url = reverse('index')
        self.client.get(url)
        self.assertEqual(visitante.status, 'AGUARDANDO')

    def test_dashboard_index_view_status_is_em_visita(self):
        # criando visitante para teste
        visitante = self.make_visitante()
        # mudando o status
        visitante.status = 'EM_VISITA'

        # extraindo o usuario para realizar o login
        porteiro = visitante.registrado_por
        user = porteiro.usuario
        self.client.force_login(user)

        url = reverse('index')
        self.client.get(url)
        self.assertEqual(visitante.status, 'EM_VISITA')

    def test_dashboard_index_view_status_is_finalizado(self):
        # criando visitante para teste
        visitante = self.make_visitante()
        # mudando o status
        visitante.status = 'FINALIZADO'

        # extraindo o usuario para realizar o login
        porteiro = visitante.registrado_por
        user = porteiro.usuario
        self.client.force_login(user)

        url = reverse('index')
        self.client.get(url)
        self.assertEqual(visitante.status, 'FINALIZADO')
