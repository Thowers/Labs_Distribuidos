from django.urls import path, include
from . import views

urlpatterns = [ 
    path("visor", views.fotos, name="fotos"),
]