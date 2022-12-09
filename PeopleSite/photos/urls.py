from django.urls import path, include

from PeopleSite.photos.views import PhotoAddView, PhotoDetailsView, PhotoEditView, PhotoDeleteView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='photo details'),
        path('edit/', PhotoEditView.as_view(), name='photo edit'),
        path('delete/', PhotoDeleteView.as_view(), name='photo delete'),
    ])
         ),
)
