from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth_app/', views.auth_app, name='auth_app'),
    path('connexion/', views.connexion, name='connexion'),
]
