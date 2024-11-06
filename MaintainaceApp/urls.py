# yourapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('update_server/', views.update_server_view, name='update_server'),
    path('/', views.homepage_view, name='homepage'),
]