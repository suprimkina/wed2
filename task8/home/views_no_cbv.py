from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import login
from django.urls import reverse, NoReverseMatch



# Create your views here.
def home(request):
    apps_names_urls = [
        {"name": "app1", "url": "app1:index"},
    ]
    context = {"app_names_urls": apps_names_urls}
    # for app in apps.get_app_configs():
    #     app_name = app.name
    #     if app_name == "home" or "django" in app_name:
    #         continue
    #     apps_names_urls.append(
    #         {"name": app_name, "url": f"{app_name}:index"}
    #     )
    #     # try:
    #     #     reverse(f"{app_name}")
    #     #     app_names.append(app_name)
    #     # except NoReverseMatch:
    #     #     continue
    # context = {"app_names_urls": apps_names_urls}
    return render(request, template_name="home/home.html", context=context)
