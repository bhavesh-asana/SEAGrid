from django.urls import path
from . import views

urlpatterns = [
    path('ExpDB/', views.client),
]