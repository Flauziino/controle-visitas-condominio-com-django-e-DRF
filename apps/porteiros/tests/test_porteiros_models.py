from porteiros.tests.test_base import BaseTest

from django.core.exceptions import ValidationError


class PorteirosModelsTest(BaseTest):
    def test_porteiro_model_string_representation(self):
        porteiro = self.make_porteiro()
        self.assertEqual(
            str(porteiro), porteiro.nome_completo
        )

    def test_porteiro_model_nome_completo_field_max_length_lt_194(self):
        porteiro = self.make_porteiro()
        porteiro.nome_completo = 'A' * 197

        with self.assertRaises(ValidationError):
            porteiro.full_clean()

    def test_porteiro_model_cpf_field_max_length_lt_11(self):
        porteiro = self.make_porteiro()
        porteiro.cpf = '1' * 15

        with self.assertRaises(ValidationError):
            porteiro.full_clean()

    def test_porteiro_model_telefone_field_max_length_lt_11(self):
        porteiro = self.make_porteiro()
        porteiro.telefone = '1' * 15

        with self.assertRaises(ValidationError):
            porteiro.full_clean()
