from django import forms
from django.contrib.auth import get_user_model

from PeopleSite.accounts.models import Gender
from PeopleSite.common.models import PhotoComment, MessagePerson

UserModel = get_user_model()

GENDER_EMPTY = [('','---------')] + Gender.choices()

class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchForm(forms.Form):
    age_lower = forms.IntegerField(required=False)
    age_higher = forms.IntegerField(required=False)
    gender = forms.ChoiceField(choices=GENDER_EMPTY, required=False)


class MessageCreateForm(forms.ModelForm):
    class Meta:
        fields = ('message',)
        model = MessagePerson
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 10,
                    'placeholder': 'Add message...'
                },
            ),
        }