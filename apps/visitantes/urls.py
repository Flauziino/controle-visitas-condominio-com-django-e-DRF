from django.urls import path
from .views import site, api


urlpatterns = [
    path(
        "registrar-visitante/",
        site.RegistrarVisitanteView.as_view(),
        name="registrar_visitante"
    ),

    path(
        "visitantes/<int:id>",
        site.InformacoesVisitante.as_view(),
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita",
        site.FinalizarVisitaView.as_view(),
        name="finalizar_visita"
    ),

    # API #
    path(
        'index-api',
        api.IndexAPIView.as_view(),
        name='index_api'
    ),
]
