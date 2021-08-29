from core.models import Planilha
from datetime import datetime, timedelta
from django.conf import settings
import os
import decimal
import pandas as pd
import model_facilities_control as mfc


class FacilitiesReport:
    """
        To Do
        Create a description here.
    """

    def __init__(self, spreadsheet):

        self.spreadsheet = spreadsheet

    def read_spreadsheet(self):
        import pandas as pd

        xls_file = self.spreadsheet
        df = pd.read_excel(xls_file)
        df = pd.DataFrame(pd.read_excel(xls_file, header=0, index_col=False))
        df = df.to_dict("records")

        return df

    def print_spreadsheet(self, df):

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


ab = FacilitiesReport(
    spreadsheet=mfc)
rab = ab.read_spreadsheet()
ab.print_spreadsheet(rab)
