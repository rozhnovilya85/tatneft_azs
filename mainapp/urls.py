# mainapp/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('api/tatneftazs/', views.GetAzsInfoView.as_view()),
]