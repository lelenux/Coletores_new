from django.urls import path
from .views import *


urlpatterns = [
    path('', login, name='login'),
    path('logout/', my_logout, name='logout'),
]

