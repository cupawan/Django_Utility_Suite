from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/', include('GoogleTranslationApp.urls')),
    path('dev/', include('RedditPostsApp.urls')),
    path('dev/', include('YouTubeToolsApp.urls')),
    path('health/', include('DailyActivityLoggerApp.urls')),
    ]
