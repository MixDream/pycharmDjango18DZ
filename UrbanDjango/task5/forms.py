from django import forms
from django.core.validators import RegexValidator
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")

    # Добавляем валидатор для возраста
    age_validator = RegexValidator(regex=r'^\d{1,3}$', message="Введите корректный возраст (0-120).")
    age = forms.IntegerField(
        max_value=120,
        min_value=0,
        label="Введите свой возраст",
        validators=[age_validator]
    )