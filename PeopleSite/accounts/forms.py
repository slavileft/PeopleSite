from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

UserModel = get_user_model()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'gender', 'password1', 'password2')

        # field_classes = {'username': UsernameField}
        # widgets={'username': forms.TextInput}
