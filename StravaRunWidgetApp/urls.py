
from django.urls import path
from . import views

urlpatterns = [
    path('strava/', views.translate_text, name='strava_widget')
    ]
