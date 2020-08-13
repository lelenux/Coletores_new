from django.urls import path
from .views import *


urlpatterns = [
    path('add/coletor/', addcoletor, name='addcoletor'),
    path('add/user/', adduser, name='adduser'),
    path('controle/', controle, name='controle'),
    path('search/user/<str:cracha>', search_user, name='search'),
    path('update/<int:id>', coletor_retirada, name='coletor_retirada'),
    path('search/coletor/<int:codigo>', search_coletor, name='search_coletor'),
    path('listar_controles/', listar_controles, name='listar_controles'),
    path('busca_coletor/', busca_coletor, name='busca_coletor'),
    path('entrega/<int:id>/', entrega_coletor, name="entrega_coletor"),
    path('update/<int:id>/', coletor_update, name="coletor_update"),
    path('voltar/<int:id>/', voltar_coletor, name="voltar_coletor"),
    path('history/', history, name="history"),
    path('coletores_list/', listar_coletores, name="coletores_list"),
    path('listar_users/', listar_users, name="listar_users"),
    path('status_coletor_update/<int:id>/', status_coletor_update, name="status_coletor_update"),
    path('status_users_update/<int:id>/', status_users_update, name="status_users_update"),
    path('observacao/<int:id>/', observacao, name="observacao"),
    #primeira opeção trago a url + um ID / na segunda o nome da minha view com as regras. e terceiro um alias.
]