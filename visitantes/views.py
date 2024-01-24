from django.shortcuts import render


def registrar_visitante(request):

    contexto = {}

    return render(
        request,
        "registrar_visitante.html",
        contexto,
    )
