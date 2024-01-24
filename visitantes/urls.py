from django.urls import path
from . import views


urlpatterns = [
    path(
        "registrar-visitante/",
        views.registrar_visitante,
        name="registrar_visitante"
    ),

    path(
        "visitantes/<int:id>",
        views.informacoes_visitante,
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita",
        views.finalizar_visita,
        name="finalizar_visita"
    ),
]
