from django.contrib import admin
from django.urls import path
from api.views import PlanilhaListAPI, PlanilhaDetailAPI, PlanilhaDeleteAPI
from core.views import list_all_xls, list_details_xls, add_xls, delete_xls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list-all-xls/', list_all_xls, name='list-all-xls'),
    path('list-details-xls/<int:id>', list_details_xls, name='list-details-xls'),

    path('add-xls', add_xls, name='add-xls'),
    path('delete-xls/<int:id>', delete_xls, name='delete-xls'),

    # To do list:
    path("api/list_planilhas", PlanilhaListAPI.as_view(), name="api-planilha-list"),
    path("api/list-details-xls/<int:id>", PlanilhaDetailAPI.as_view(), name="api-planilha-details"),
    path("api/delete-planilha/<int:id>", PlanilhaDeleteAPI.as_view(), name="api-delete-planilha"),
]
