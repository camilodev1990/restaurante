from django.urls import path
from aplicaciones.usuarios import views

urlpatterns = [
    path('', views.base, name='base')
]
