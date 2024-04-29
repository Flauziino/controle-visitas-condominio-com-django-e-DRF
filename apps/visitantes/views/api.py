from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.db.models import Min
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404

from visitantes.serializers import (
    VisitanteSerializer, AutorizaVisitanteSerializer
)
from visitantes.models import Visitante


class IndexAPIView(APIView):
    # permission_classes = [IsAuthenticated,]
    http_method_names = ['get',]

    def get(self, request):
        hora_atual = timezone.now()
        mes_atual = hora_atual.month

        todos_visitantes = Visitante.objects.order_by(
            "-horario_chegada"
        )

        visitantes_aguardando = todos_visitantes.filter(
            status="AGUARDANDO"
        )

        visitantes_em_visita = todos_visitantes.filter(
            status="EM_VISITA"
        )

        visitantes_finalizado = todos_visitantes.filter(
            status="FINALIZADO"
        )

        visitante_mes = todos_visitantes.filter(
            horario_chegada__month=mes_atual
        )

        todos_visitantes_data = VisitanteSerializer(
            todos_visitantes, many=True).data

        data = {
            "nome_pagina": "Início da dashboard",
            "todos_visitantes": todos_visitantes_data,
            "visitantes_aguardando": visitantes_aguardando.count(),
            "visitantes_em_visita": visitantes_em_visita.count(),
            "visitantes_finalizado": visitantes_finalizado.count(),
            "visitante_mes": visitante_mes.count(),
        }

        return Response(data)
