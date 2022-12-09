from django import forms


class ThreadForm(forms.Form):
  username = forms.CharField(label='', max_length=100)
  username.widget = username.hidden_widget()


class MessageForm(forms.Form):
  message = forms.CharField(label='', max_length=1000)