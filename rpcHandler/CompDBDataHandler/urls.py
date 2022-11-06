from django.urls import path
from . import views

urlpatterns = [
    path('CompDB/', views.client),
]