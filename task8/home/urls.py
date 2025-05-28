from django.urls import include, path, reverse, NoReverseMatch
from django.apps import apps
from django.shortcuts import redirect

from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
