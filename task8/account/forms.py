from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from datetime import date

from .models import CustomUser, Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'

    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        if len(username) < 3:
            raise ValidationError(
                message=f"username length < 3",
                code="username length < 3"
            )
        if ' ' in username:
            raise ValidationError(
                message="There should be no spaces in the password",
                code="invalid password"
            )
        return username


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'

    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        if len(username) < 3:
            raise ValidationError(
                message=f"username length < 3",
                code="username length < 3"
            )
        if ' ' in username:
            raise ValidationError(
                message="There should be no spaces in the password",
                code="invalid password"
            )
        return username


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', max_length=32)

    class Meta:
        model = Profile
        fields = ['avatar', 'username', 'birthday', 'bio']
        labels = {
            'avatar': 'Фото профиля',
            'birthday': 'День рождения',
            'bio': 'О себе',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['birthday'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        # if self.instance.user.username == username:
        #     raise forms.ValidationError(
        #         message="That's your actual username",
        #         code='user actual username'
        #     )
        if CustomUser.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                message='Username already exists',
                code='username already exists'
            )
        return username

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if birthday and not (date(year=1900, month=1, day=1) <= birthday <= date.today()):
            raise ValidationError(
                'Invalid birthday',
                code='invalid bday'
            )

        return birthday

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.avatar = self.cleaned_data.get('avatar')
        username = self.cleaned_data.get('username')
        if commit:
            if username != profile.user.username:
                profile.user.username = username
                profile.user.save()
            profile.save()
        return profile
