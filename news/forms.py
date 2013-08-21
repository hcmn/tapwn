from django import forms
from tapwn.news.models import Headline

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())