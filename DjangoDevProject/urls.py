from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('/', include('MaintainanceApp.urls')),
    path('dev/', include('GoogleTranslationApp.urls')),
    path('dev/', include('RedditPostsApp.urls')),
    path('dev/', include('YouTubeToolsApp.urls')),
    path('dev/', include('MaintainaceApp.urls')),
    path('dev/', include('DailyActivityLoggerApp.urls')),
    ]
