"""proyecto_django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Series import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear-serie/<str:serie_name>/<str:serie_clasificacion>/<str:serie_num_capitulos>/<str:serie_num_temporadas>', views.crear_series, name="crear_series"),
    path('serie/', views.serie, name="serie"),
    path('actualizar-serie/<int:id>', views.actualizar_Serie, name="actualizar_Serie"),
    path('serie-found/<int:id>', views.Serie_Found, name="serie_found"),
    path('series/', views.all_series, name="series"),
    path('delete-serie/<int:id>', views.delete_serie, name="delete_serie"),
]
