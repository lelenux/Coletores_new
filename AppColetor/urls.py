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
    path('entrega/<int:id>/', entrega_coletor, name="entrega_coletor"),
    path('update/<int:id>/', coletor_update, name="coletor_update"),
    path('voltar/<int:id>/', voltar_coletor, name="voltar_coletor"),
    path('history/', history, name="history"),

    # path('saida/<int:id>/', saida_update, name="saida_update"),
]