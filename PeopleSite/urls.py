from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PeopleSite.common.urls')),
    path('accounts/', include('PeopleSite.accounts.urls')),
    path('photos/', include('PeopleSite.photos.urls')),
    path('chat/', include('PeopleSite.chat.urls')),
]
