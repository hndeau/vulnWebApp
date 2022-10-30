"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from .settings import MEDIA_ROOT
from .views import home, css_main, file_upload
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('css/main.css', css_main, name='css_main'),
    path('accounts/', include("accounts.urls")),
    path('upload', file_upload, name='upload'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)

