from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    nome_completo = forms.CharField(
        label="Nome Completo",
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite o nome completo'}),
        error_messages={
            "required": "O nome completo do visitante é obrigatório para o registro."  # noqa: E501
        }
    )

    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(attrs={'placeholder': 'Digite o CPF'}),
        error_messages={
            "required": "O CPF do visitante é obrigatório para o registro."
        }
    )

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={'placeholder': 'AAAA-MM-DD'}),
        error_messages={
            "required": "A data de nascimento do visitante é obrigatório para o registro",  # noqa: E501
            "invalid": "Por favor, informe um formato válido para a data de nascimento. Ex:(AAAA-MM-DD)"  # noqa: E501
        }
    )

    numero_casa = forms.CharField(
        label="Número da Casa",
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite o número da casa a ser visitada'}),
        error_messages={
            "required": "Por favor, informe o número da casa a ser visitada."
        }
    )

    placa_veiculo = forms.CharField(
        label="Placa do Veículo",
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite o número da placa do veículo'}),
        required=False
    )

    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]


class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(
        label="Morador Responsável",
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do morador responsável'}),  # noqa: E501
        error_messages={
            "required": "Por favor, informe o nome do morador responsável."
        }
    )

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
