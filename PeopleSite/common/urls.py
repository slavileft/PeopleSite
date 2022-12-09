from django.urls import path

from PeopleSite.common.views import index, like_photo, comment_photo, about_view

urlpatterns = (
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('like/<int:photo_id>/', like_photo, name='photo like'),
    path('comments/<int:photo_id>/', comment_photo, name='photo comment'),
)
