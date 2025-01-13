
from django.urls import path
from . import views

urlpatterns = [
    path('running/', views.get_strava, name='run_widget'),
    path('get_run_ids/', views.get_run_ids, name='get_run_ids')
    ]
