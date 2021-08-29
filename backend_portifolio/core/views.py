from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from core.models import Planilha
import pandas as pd

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
                "file": p.file,
                "data": p.data,
            }
        )

    context = {"planilha": lista, "title": 'Planilhas'}

    print(context)

    return render(request, "planilha/planilha_list.html", context)


def list_details_xls(request, id):

    xls = Planilha.objects.get(id=id)
    xls_file = xls.file
    df = pd.DataFrame(pd.read_excel(xls_file, header=0, index_col=False))
    df = df.to_dict("split")

    Region = 0
    BuidingId = 1
    CostCentre = 2
    TelcoCode = 3
    BuildingCurrentUse = 4
    Country = 5
    LocalCurrencyName = 6
    CostDate = 7
    BudFXRate = 8
    RentLCY = 9
    UtilitiesLCY = 10
    FacilityLCY = 11
    SuppliesLCY = 12

    lista = []
    for x in df['data']:

        entry = {
            'Region': x[Region],
            'BuidingId': x[BuidingId],
            'CostCentre': x[CostCentre],
            'TelcoCode':  x[TelcoCode],
            'BuildingCurrentUse': x[BuildingCurrentUse],
            'Country': x[Country],
            'LocalCurrencyName': x[LocalCurrencyName],
            'CostDate': str(x[CostDate]),
            'BudFXRate': x[BudFXRate],
            'RentLCY':  x[RentLCY],
            'UtilitiesLCY': x[UtilitiesLCY],
            'FacilityLCY': x[FacilityLCY],
            'SuppliesLCY': x[SuppliesLCY],
        }
        lista.append(entry)

    print(lista)

    context = {'context': lista}

    return render(request, "planilha/planilha_details.html", context)
