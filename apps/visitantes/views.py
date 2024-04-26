from django.views import View
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Visitante
from .forms import VisitanteForm, AutorizaVisitanteForm


class MyBaseView(View):
    def get_visitante(self, id):
        visitante = get_object_or_404(Visitante, id=id)
        return visitante


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class RegistrarVisitanteView(CreateView):
    model = Visitante
    form_class = VisitanteForm
    template_name = "registrar_visitante.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        visitante = form.save(commit=False)

        visitante.registrado_por = self.request.user.porteiro
        visitante.save()

        messages.success(
            self.request,
            "Visitante registrado com sucesso!"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "nome_pagina": "Registrar visitante",
        })

        return ctx


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class InformacoesVisitante(MyBaseView):
    def render_ctx(self, visitante, form):
        ctx = {
            "nome_pagina": "Informações de visitante",
            "visitante": visitante,
            "form": form,
        }

        return render(
            self.request,
            "informacoes_visitante.html",
            ctx
        )

    def get(self, request, id):
        form = AutorizaVisitanteForm()
        visitante = self.get_visitante(id)
        return self.render_ctx(visitante, form)

    def post(self, request, id):
        visitante = self.get_visitante(id)
        form = AutorizaVisitanteForm(request.POST, instance=visitante)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()
            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")
        return self.render_ctx(visitante, form)


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class FinalizarVisitaView(MyBaseView):
    def post(self, request, id):
        visitante = self.get_visitante(id)
        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect('index')
