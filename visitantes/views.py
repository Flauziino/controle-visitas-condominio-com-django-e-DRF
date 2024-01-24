from django.shortcuts import render
from .forms import VisitanteForm


def registrar_visitante(request):

    form = VisitanteForm()
    contexto = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(
        request,
        "registrar_visitante.html",
        contexto,
    )
