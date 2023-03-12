from django.urls import path
from .views_commande import CommandeController
from .views_depot import DepotController
urlpatterns = [

    #pour les commandes

    path('all/', CommandeController.api_view_get_all, name='api_view_get_all'),
    path('add/', CommandeController.api_view_post, name='api_view_post'),
    path('<str:code>/', CommandeController.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', CommandeController.api_view_put, name='api_view_put'),

    #pour les dépôt

    path('all/', DepotController.api_view_get_all, name='api_view_get_all'),
    path('add/', DepotController.api_view_post, name='api_view_post'),
    path('<str:code>/', DepotController.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', DepotController.api_view_put, name='api_view_put'),
]
