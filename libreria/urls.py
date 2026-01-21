from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),    
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('editar_libro/', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/', views.eliminar_libro, name='eliminar_libro'),
    path('detalle_libro/', views.detalle_libro, name='detalle_libro'),
]   