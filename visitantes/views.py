from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import VisitanteForm
from .models import Visitante


def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(
                request,
                "Visitante registrado com sucesso!"
            )

            return redirect(
                "index"
            )

    contexto = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(
        request,
        "registrar_visitante.html",
        contexto,
    )


def informacoes_visitante(request, id):

    visitante = get_object_or_404(
        Visitante,
        id=id
    )

    contexto = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitante
    }

    return render(
        request,
        "informacoes_visitante.html",
        contexto
    )
