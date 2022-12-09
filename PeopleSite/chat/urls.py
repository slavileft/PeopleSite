from django.urls import path

from PeopleSite.chat.views import ListThreads, CreateThread, CreateMessage, ThreadView

urlpatterns = (
    path('', ListThreads.as_view(), name='inbox'),
    path('<int:pk>/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('<int:pk>/', ThreadView.as_view(), name='thread'),
    path('<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
)