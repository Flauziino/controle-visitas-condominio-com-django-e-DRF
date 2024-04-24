from unittest import TestCase

from django.urls import reverse

from visitantes import forms
from porteiros.tests.test_base import BaseTest

from parameterized import parameterized


class VisitantesFormsTest(BaseTest):
    def setUp(self):
        self.form_data = {
            "nome_completo": 'Test',
            "cpf": '11133322245',
            "data_nascimento": '1993-05-15',
            "numero_casa": '100',
            "placa_veiculo": '1234567'
        }
    # ////////////////// #
    # FORM VisitanteForm #

    @parameterized.expand([
        ('nome_completo', 'Nome Completo'),
        ('cpf', 'CPF'),
        ('data_nascimento', 'Data de Nascimento'),
        ('numero_casa', 'Número da Casa'),
        ('placa_veiculo', 'Placa do Veículo'),
    ])
    def test_visitante_form_field_label(self, field, needed):
        form = forms.VisitanteForm()
        current = form[field].field.label

        self.assertEqual(current, needed)

    @parameterized.expand([
        ('nome_completo', 'Digite o nome completo'),
        ('cpf', 'Digite o CPF'),
        ('data_nascimento', 'AAAA-MM-DD'),
        ('numero_casa', 'Digite o número da casa a ser visitada'),
        ('placa_veiculo', 'Digite o número da placa do veículo'),
    ])
    def test_visitante_form_field_placeholder(self, field, needed):
        form = forms.VisitanteForm()
        current = form[field].field.widget.attrs['placeholder']

        self.assertEqual(current, needed)

    @parameterized.expand([
        ('nome_completo', "O nome completo do visitante é obrigatório para o registro."),  # noqa: E501
        ('cpf', "O CPF do visitante é obrigatório para o registro."),
        ('data_nascimento', "A data de nascimento do visitante é obrigatório para o registro"),  # noqa: E501
        ('numero_casa', "Por favor, informe o número da casa a ser visitada."),
    ])
    def test_visitante_form_fields_cannot_be_empty(self, field, msg):
        self.make_porteiro()
        self.form_data[field] = ''

        url = reverse('registrar_visitante')
        response = self.client.post(url, data=self.form_data)

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_visitante_form_field_data_nascimento_with_invalid_value(self):
        self.make_porteiro()
        self.form_data['data_nascimento'] = '21031993'

        url = reverse('registrar_visitante')
        response = self.client.post(url, data=self.form_data)

        self.assertIn(
            "Por favor, informe um formato válido para a data de nascimento. Ex:(AAAA-MM-DD)",  # noqa: E501
            response.content.decode('utf-8')
        )
