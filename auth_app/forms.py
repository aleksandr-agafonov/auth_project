from django import forms
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class CallTouchForm(forms.Form):
    node = forms.CharField()
    cabinet_id = forms.CharField()
    calltouch_token = forms.CharField()
    start_date = forms.CharField(empty_value=(datetime.now() - timedelta(days=1)))