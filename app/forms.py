from django import forms
from app.models import User, Question, Answer
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


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
        fields = ['first_name', 'last_name', 'username', 'email']


class AskForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.TextInput()
    tags = forms.CharField()

    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']


class AnswerForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': 4,
                                                        'placeholder': 'Write your answer'}))

    class Meta:
        model = Answer
        fields = ['text']


class SettingsForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    avatar = forms.ImageField(required=False, widget=forms.FileInput)

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('user', None)
        super(SettingsForm, self).__init__(*args, **kwargs)

    # def clean_username(self):
    #     user = User.objects.filter(username=self.cleaned_data['username'])
    #     if user and (user.get().id != self.current_user.id):
    #         raise ValidationError(_(u"This username has already been taken"))
    #     return self.cleaned_data['username']
    def clean(self):
        user = User.objects.filter(username=self.cleaned_data['username'])
        if user and (user.get().id != self.current_user.id):
            msg = u"This username has already been taken!"
            self._errors["username"] = self.error_class([msg])
        return self.cleaned_data


    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')


