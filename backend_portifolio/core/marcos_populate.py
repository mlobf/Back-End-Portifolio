from core.models import Planilha
import pandas as pd
import json


xls = Planilha.objects.last()
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

json_lists = json.dumps(lista)

xls.data = json_lists
xls.save()
