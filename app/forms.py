from django import forms
from app.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_confirm = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
