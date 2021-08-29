from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from core.models import Planilha

# Create your views here.


def list_all_xls(request):
    lista = []
    planilhas = Planilha.objects.all()
    for p in planilhas:
        lista.append(
            {
                "id": p.pk,
                "created_at": p.created,
                "external_key": p.external_key,
                "client_name": p.client_name,
                "data": p.data,
            }
        )

    context = {"planilha": lista, "title": 'Planilhas'}
    return render(request, "planilha/list_by_descricao_planilha.html", context)
