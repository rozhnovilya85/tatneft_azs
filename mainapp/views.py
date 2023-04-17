from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AzsDB
from .serializers import Tatneft_azs

class GetAzsInfoView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы
        queryset = AzsDB.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = Tatneft_azs(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)