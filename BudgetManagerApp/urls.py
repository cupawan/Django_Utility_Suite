from django.urls import path
from . import views

urlpatterns = [
    path('expense/', views.log_view, name='daily_spend_log'),
]