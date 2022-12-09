from django.urls import path, include

from PeopleSite.common.views import index, like_photo, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='photo like'),
    path('comments/<int:photo_id>/', comment_photo, name='photo comment'),
)
