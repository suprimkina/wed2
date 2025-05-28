"""
URL configuration for practice_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import static
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('app1/', include('app1.urls')),
    path('account/', include('account.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# нельзя так делать при серьезном проекте
# for app in apps.get_app_configs():
#     app_name = app.name
#     if app_name != "home" and "django" not in app_name:
#         urlpatterns.append(
#             path(f'{app_name}/', include(f'{app_name}.urls'))
#         )
#
#     # try:
#     #     reverse(f"{app_name}")
#     #     app_names.append(app_name)
#     # except NoReverseMatch:
#     #     continue
