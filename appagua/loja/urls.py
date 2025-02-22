from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # URLs para Usuario
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    # URLs para Cliente
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    # URLs para Entregador
    path('entregadores/', views.listar_entregadores, name='listar_entregadores'),
    # URLs para Produto
    path('produtos/', views.listar_produtos, name='listar_produtos'),
]
