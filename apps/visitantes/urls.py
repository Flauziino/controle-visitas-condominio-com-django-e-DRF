from django.urls import path
from . import views


urlpatterns = [
    path(
        "registrar-visitante/",
        views.RegistrarVisitanteView.as_view(),
        name="registrar_visitante"
    ),

    path(
        "visitantes/<int:id>",
        views.InformacoesVisitante.as_view(),
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita",
        views.FinalizarVisitaView.as_view(),
        name="finalizar_visita"
    ),
]
