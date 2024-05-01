from collections import defaultdict

from rest_framework import serializers

from visitantes.models import Visitante


class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = [
            "id", "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]

    nome_completo = serializers.CharField()
    cpf = serializers.CharField()
    data_nascimento = serializers.DateField()
    numero_casa = serializers.CharField()
    placa_veiculo = serializers.CharField(required=False)

    def validate(self, attrs):
        super_validade = super().validate(attrs)
        cleaned_data = attrs

        errors = defaultdict(list)

        nome_completo = cleaned_data.get('nome_completo')
        cpf = cleaned_data.get('cpf')
        numero_casa = cleaned_data.get('numero_casa')

        if len(nome_completo) < 5:
            errors['nome_completo'].append(
                'Por favor, digite o nome completo do visitante'
            )

        if len(cpf) != 11:
            errors['cpf'].append(
                'Por favor, digite um cpf válido (11 digitos)'
            )

        if numero_casa is None or numero_casa == '':
            errors['numero_casa'].append(
                'Por favor, digite o número da casa a ser visitada'
            )

        if errors:
            raise serializers.ValidationError(errors)
        return super_validade


class AutorizaVisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = [
            "id", "morador_responsavel"
        ]

    morador_responsavel = serializers.CharField()

    def validate(self, attrs):
        super_validade = super().validate(attrs)
        cleaned_data = attrs

        errors = defaultdict(list)

        morador_responsavel = cleaned_data.get('morador_responsavel')
        if morador_responsavel is None or morador_responsavel == '':
            errors['morador_responsavel'].append(
                'É preciso digitar o nome do morador responsável pela autorização'  # noqa: E501
            )

        if errors:
            raise serializers.ValidationError(errors)
        return super_validade
