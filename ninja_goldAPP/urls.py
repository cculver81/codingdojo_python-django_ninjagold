from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('farm_click', views.farm_click),
    path('cave_click', views.cave_click),
    path('house_click', views.house_click),
    path('casino_click', views.casino_click)
]