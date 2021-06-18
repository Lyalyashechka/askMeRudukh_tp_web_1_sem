from django import forms
from app.models import User, Question


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class AskForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.TextInput()
    tags = forms.CharField()
    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']
