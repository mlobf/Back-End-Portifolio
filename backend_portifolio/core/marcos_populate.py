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


lista = []
for x in df['data']:
    print('       ------------------------     ')
    print((x[Region]))
    print((x[BuidingId]))
    print((x[CostCentre]))
    print((x[TelcoCode]))
    print((x[BuildingCurrentUse]))
    print((x[Country]))
    print((x[LocalCurrencyName]))
    print((x[CostDate]))
    print((x[BudFXRate]))
    print((x[RentLCY]))
    print((x[UtilitiesLCY]))
    print((x[FacilityLCY]))
    print((x[SuppliesLCY]))


# xls.data = df
# xls.save()


# TypeError: Object of type DataFrame is not JSON serializable
# df_json = json.dumps(df)


'''
count = 0
for _ in df:
    print(
        df[count]["Region"],
        df[count]["BuidingId"],
        df[count]["CostCentre"],
        df[count]["TelcoCode"],
        df[count]["BuildingCurrentUse"],
        df[count]["Country"],
        df[count]["LocalCurrencyName(LCY)"],
        df[count]["CostDate"],
        df[count]["2010BudFXRate"],
        df[count]["RentLCY"],
        df[count]["UtilitiesLCY"],
        df[count]["FacilityLCY"],
        df[count]["SuppliesLCY"],
    )
    count = count + 1
'''
