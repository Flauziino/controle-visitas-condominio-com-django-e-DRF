from porteiros.tests.test_base import BaseTest

from parameterized import parameterized

from django.utils import timezone
from django.core.exceptions import ValidationError


class VisitantesModelsTest(BaseTest):
    def test_visitantes_model_string_representation(self):
        visitante = self.make_visitante()
        self.assertEqual(
            str(visitante), visitante.nome_completo
        )

    def test_visitantes_model_status_is_aguardando_by_default(self):
        visitante = self.make_visitante_with_no_default()
        self.assertEqual(visitante.status, 'AGUARDANDO')

    def test_visitantes_model_status_field_max_length(self):
        visitante = self.make_visitante()
        self.assertEqual(
            visitante._meta.get_field('status').max_length,
            10
        )

    @parameterized.expand([
        ('nome_completo', 200),
        ('cpf', 15),
        ('placa_veiculo', 10),
        ('morador_responsavel', 200)
    ])
    def test_visitantes_models_fields_max_length(self, field, max_length):
        visitante = self.make_visitante()
        setattr(visitante, field, 'A' * max_length)

        with self.assertRaises(ValidationError):
            visitante.full_clean()

    def test_get_horario_de_saida_method_have_horario_saida(self):
        hoje = timezone.now().date()
        visitante = self.make_visitante()
        visitante.horario_saida = hoje

        self.assertEqual(
            visitante.get_horario_saida(),
            visitante.horario_saida
        )

    def test_get_horario_de_saida_method_without_horario_saida(self):
        visitante = self.make_visitante()

        self.assertEqual(
            visitante.get_horario_saida(),
            "Horário de saída não registrado"
        )

    def test_get_horario_de_autorizacao_method_have_horario_de_autorizacao(self):  # noqa: E501
        hoje = timezone.now().date()
        visitante = self.make_visitante()
        visitante.horario_autorizacao = hoje

        self.assertEqual(
            visitante.get_horario_autorizacao(),
            visitante.horario_autorizacao
        )

    def test_get_horario_de_autorizacao_method_without_horario_de_autorizacao(self):  # noqa: E501
        visitante = self.make_visitante()

        self.assertEqual(
            visitante.get_horario_autorizacao(),
            "Visitante aguardando autorização"
        )

    def test_get_morador_responsavel_method_have_morador_responsavel(self):
        visitante = self.make_visitante()
        visitante.morador_responsavel = 'Responsavel Test'

        self.assertEqual(
            visitante.get_morador_responsavel(),
            visitante.morador_responsavel
        )

    def test_get_morador_responsavel_method_without_morador_responsavel(self):
        visitante = self.make_visitante()

        self.assertEqual(
            visitante.get_morador_responsavel(),
            "Visitante aguardando autorização"
        )

    def test_get_placa_veiculo_method_have_placa_veiculo(self):
        visitante = self.make_visitante()
        visitante.placa_veiculo = '1234567'

        self.assertEqual(
            visitante.get_placa_veiculo(),
            visitante.placa_veiculo
        )

    def test_get_placa_veiculo_method_without_placa_veiculo(self):
        visitante = self.make_visitante()

        self.assertEqual(
            visitante.get_placa_veiculo(),
            "Veículo não registrado"
        )

    def test_get_cpf_method_have_cpf(self):
        visitante = self.make_visitante()

        self.assertEqual(
            visitante.get_cpf(),
            '111.333.222-56'
        )

    def test_get_cpf_method_without_cpf(self):
        visitante = self.make_visitante()
        visitante.cpf = ''

        self.assertEqual(
            visitante.get_cpf(),
            None
        )
