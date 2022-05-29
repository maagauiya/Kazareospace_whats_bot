
from unicodedata import name
from .views import *
from django.contrib.auth import views as auth_views

from django.urls import path, include

from django.urls import path

urlpatterns = [

    path('ras/', rassylka,name='rassylka'),
    path('ras/<int:pk>/', news,name='das'),

]
