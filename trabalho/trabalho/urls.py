from django.contrib import admin
from django.urls import path
from usuarios.views import listarUsuarios, detalharUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', listarUsuarios),
    path('usuarios/<int:id>', detalharUsuario)
]
