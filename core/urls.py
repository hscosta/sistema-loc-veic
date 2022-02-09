from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Locadora de Veículos | G3 Telecom'
urlpatterns = [
    path('', admin.site.urls),
]
