from django.shortcuts import render, redirect, reverse
from core.models import Planilha
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from api.serializers import PlanilhaSerializer
# Create your views here.


class PlanilhaListAPI(APIView):

    def get(self, request):

        planilha = Planilha.objects.all()
        serializer = PlanilhaSerializer(planilha, many=True)

        return Response(serializer.data)


class PlanilhaDetailAPI(APIView):

    def get_object(self, id):
        planilha = get_object_or_404(Planilha, id=id)
        return planilha

    def get(self, request, id):
        planilha = Planilha.objects.get(id=id)
        serializer = PlanilhaSerializer(planilha)

        return Response(serializer.data)


class PlanilhaDeleteAPI(APIView):

    def get_object(self, id):
        planilha = get_object_or_404(Planilha, id=id)
        return planilha

    def get(self, request, id):
        planilha = Planilha.objects.get(id=id)
        planilha.delete()

        return redirect(reverse('api-planilha-list'))
