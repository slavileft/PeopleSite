from django.urls import path

from PeopleSite.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, \
    UserEditView, UserDetailsView, UserDeleteView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='user details'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='user edit'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user delete'),
)

from .signals import *