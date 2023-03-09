from django.urls import path
from .views_depot import DepotController


urlpatterns = [
    path('all/', DepotController.api_view_get_all, name='api_view_get_all'),
    path('add/', DepotController.api_view_post, name='api_view_post'),
    path('<str:code>/', DepotController.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', DepotController.api_view_put, name='api_view_put'),
]
