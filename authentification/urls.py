from django.urls import path
from .views import UtilisateursControllers
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('all/', UtilisateursControllers.api_view_get_all, name='api_view_get_all'),
    path('add/', UtilisateursControllers.api_view_post, name='api_view_post'),
    path('auth/login', UtilisateursControllers.api_view_post_login, name='api_view_post_login'),
     path('logged/<str:email>', UtilisateursControllers.api_view_get_email, name='api_view_get_email'),
    path('<str:code>/', UtilisateursControllers.api_view_get_code, name='api_view_get_code'),
    path('<str:code>/', UtilisateursControllers.api_view_put, name='api_view_put'),
    path('auth', obtain_auth_token),
]
