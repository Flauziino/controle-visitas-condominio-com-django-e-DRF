from django.urls import path
from .views import site, api

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


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

    path(
        "registrar-visitante-api/",
        api.RegistrarVisitanteAPIView.as_view(),
        name="registrar_visitante_api"
    ),

    path(
        'visitantes-api/<int:id>',
        api.InformacoesVisitanteAPIView.as_view(),
        name='informacoes-visitante'
    ),

    # JWT #
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
    # Por último
]
