from django.urls import path, include
from . import views

urlpatterns = [ 
    path("visor", views.fotos, name="fotos"),
    + path('fotos/', include('apps.fotos.urls')),  # Incluye las rutas de la app fotos
]