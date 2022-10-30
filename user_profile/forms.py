from django import forms
from django.contrib.auth import forms, password_validation


class LoginForm(forms.AuthenticationForm):
    username = forms.UsernameField(widget=forms.forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'

        }
    ), label='Имя пользователя')
    password = forms.forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'class': 'form-control',
                   'placeholder': 'Введите пароль'}),
    )


class RegisterForm(forms.UserCreationForm):
    username = forms.UsernameField(widget=forms.forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Придумайте имя пользователя'
        }
    ), label='Имя пользователя', )
    password1 = forms.forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'class': 'form-control',
                   'placeholder': 'Введите пароль'}),
    )
    password2 = forms.forms.CharField(
        label="Подтвердите пароль",
        strip=False,
        widget=forms.forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'class': 'form-control',
                   'placeholder': 'Введите пароль еще раз'}),
    )
