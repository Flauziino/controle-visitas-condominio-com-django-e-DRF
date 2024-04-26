# VIEW APP DASHBOARD
# ///////////////// #
# @login_required
# def index(request):

#     todos_visitantes = Visitante.objects.order_by(
#         "-horario_chegada"
#     )

#     visitantes_aguardando = todos_visitantes.filter(
#         status="AGUARDANDO"
#     )

#     visitantes_em_visita = todos_visitantes.filter(
#         status="EM_VISITA"
#     )

#     visitantes_finalizado = todos_visitantes.filter(
#         status="FINALIZADO"
#     )

#     hora_atual = timezone.now()
#     mes_atual = hora_atual.month

#     visitante_mes = todos_visitantes.filter(
#         horario_chegada__month=mes_atual
#     )

#     context = {
#         "nome_pagina": "Início da dashboard",
#         "todos_visitantes": todos_visitantes,
#         "visitantes_aguardando": visitantes_aguardando.count(),
#         "visitantes_em_visita": visitantes_em_visita.count(),
#         "visitantes_finalizado": visitantes_finalizado.count(),
#         "visitante_mes": visitante_mes.count(),
#     }

#     return render(
#         request,
#         "index.html",
#         context
#     )
#
#
# ////////////////////
# VIEWS APP VISITANTES
# /////////////////////
# @login_required
# def registrar_visitante(request):

#     form = VisitanteForm()

#     if request.method == 'POST':
#         form = VisitanteForm(request.POST)

#         if form.is_valid():
#             visitante = form.save(commit=False)

#             visitante.registrado_por = request.user.porteiro
#             visitante.save()

#             messages.success(
#                 request,
#                 "Visitante registrado com sucesso!"
#             )

#             return redirect(
#                 "index"
#             )

#     contexto = {
#         "nome_pagina": "Registrar visitante",
#         "form": form
#     }

#     return render(
#         request,
#         "registrar_visitante.html",
#         contexto,
#     )
#
#
# ////////////////////////
# ////////////////////////
# @login_required
# def informacoes_visitante(request, id):

#     visitante = get_object_or_404(
#         Visitante,
#         id=id
#     )

#     form = AutorizaVisitanteForm()

#     if request.method == 'POST':
#         form = AutorizaVisitanteForm(
#             request.POST,
#             instance=visitante
#         )

#         if form.is_valid():
#             visitante = form.save(commit=False)

#             visitante.status = "EM_VISITA"
#             visitante.horario_autorizacao = timezone.now()

#             visitante.save()

#             messages.success(
#                 request,
#                 "Entrada de visitante autorizada com sucesso"
#             )

#             return redirect("index")

#     contexto = {
#         "nome_pagina": "Informações de visitante",
#         "visitante": visitante,
#         "form": form,
#     }

#     return render(
#         request,
#         "informacoes_visitante.html",
#         contexto
#     )
#
#
# ////////////////////////////
# ///////////////////////////
# @login_required
# def finalizar_visita(request, id):
#     if request.method == 'POST':
#         visitante = get_object_or_404(
#             Visitante,
#             id=id
#         )

#         visitante.status = "FINALIZADO"
#         visitante.horario_saida = timezone.now()

#         visitante.save()

#         messages.success(
#             request,
#             "Visita finalizada com sucesso"
#         )

#         return redirect('index')

#     else:
#         return HttpResponseNotAllowed(
#             ["POST"],
#             "Método não permitido"
#         )
