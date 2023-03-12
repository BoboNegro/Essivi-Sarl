from django.urls import path
from .views_marque import MarqueController
from .views_produits import ProduitController

urlpatterns = [

    #pour les commandes

    path('all/', MarqueController.api_view_get_all, name='api_view_get_all'),
    path('add/', MarqueController.api_view_post, name='api_view_post'),
    path('<str:code>/', MarqueController.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', MarqueController.api_view_put, name='api_view_put'),

    #pour les dépôt

    path('all/', ProduitController.api_view_get_all, name='api_view_get_all'),
    path('add/', ProduitController.api_view_post, name='api_view_post'),
    path('<str:code>/', ProduitController.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', ProduitController.api_view_put, name='api_view_put'),
]
