"""
URL configuration for isobest project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls")),
]

if settings.DEBUG:
    # Sert les fichiers static/ directement (utile en hébergement WSGI type Hostinger,
    # où le serveur ne les sert pas automatiquement comme le fait `runserver`).
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static_serve, {
            'document_root': settings.BASE_DIR / 'myapp' / 'static',
        }),
    ]
