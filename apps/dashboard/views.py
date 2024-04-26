from django.utils import timezone
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from visitantes.models import Visitante


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

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

        ctx.update({
            "nome_pagina": "Início da dashboard",
            "todos_visitantes": todos_visitantes,
            "visitantes_aguardando": visitantes_aguardando.count(),
            "visitantes_em_visita": visitantes_em_visita.count(),
            "visitantes_finalizado": visitantes_finalizado.count(),
            "visitante_mes": visitante_mes.count(),
        })

        return ctx
