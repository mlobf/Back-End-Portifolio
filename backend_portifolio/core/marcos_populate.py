from core.models import Planilha
import pandas as pd
import json


xls = Planilha.objects.last()
xls_file = xls.file

# df = pd.read_excel(xls_file)

df = pd.DataFrame(pd.read_excel(xls_file, header=0, index_col=False))
df = df.to_dict("split")
# df = df.to_dict("records")
# df = df.to_json(orient='columns')

# df = df.to_json(orient='table')

# print(df)

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
'''
entry = {

    'Region': x[Region],
    'BuidingId': x[BuidingId],
    'CostCentre': x[CostCentre],
    'TelcoCode':  x[TelcoCode],
    'BuildingCurrentUse': x[BuildingCurrentUse],
    'Country': x[Country],
    'LocalCurrencyName': x[LocalCurrencyName],
    'CostDate': x[CostDate],
    'BudFXRate': x[BudFXRate],
    'RentLCY':  x[RentLCY],
    'UtilitiesLCY': x[UtilitiesLCY],
    'FacilityLCY': x[FacilityLCY],
    'SuppliesLCY': x[SuppliesLCY],

}
'''

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

print(lista[0])

json_lists = json.dumps(lista)
print(json_lists)


# xls.data = df
# xls.save()

# TypeError: Object of type DataFrame is not JSON serializable
# df_json = json.dumps(df)
