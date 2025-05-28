from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import login
from django.urls import reverse, NoReverseMatch
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_names_urls'] = [
            {"name": "app1", "url": "app1:index"}
        ]
        return context
