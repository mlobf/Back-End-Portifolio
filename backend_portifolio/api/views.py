from django.shortcuts import render
from core.models import Planilha
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import PlanilhaSerializer
# Create your views here.


class PlanihaListAPI(APIView):

    def get(self, request):

        planilha = Planilha.objects.all()
        serializer = PlanilhaSerializer(planilha, many=True)

        return Response(serializer.data)
