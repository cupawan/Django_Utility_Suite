# yourapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('activity/', views.daily_activity_view, name='daily_activity'),
]