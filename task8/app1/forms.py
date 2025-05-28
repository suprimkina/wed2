from django import forms
from django.core.exceptions import ValidationError
from datetime import date
import re

from .models import Application, ProgLang


class ApplicationModelForm(forms.ModelForm):
    prog_langs = forms.ModelMultipleChoiceField(
        queryset=ProgLang.objects.all(),
        widget=forms.SelectMultiple,
        label="Любимый язык программирования"
    )

    class Meta:
        model = Application
        fields = ['fio', 'telephone', 'email', 'bday', 'sex', 'prog_langs', 'biography']
        widgets = {
            'sex': forms.RadioSelect(choices=[('man', 'Мужской'), ('woman', 'Женский')]),
            'bday': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fio': 'ФИО',
            'telephone': 'Телефон',
            'email': 'Email',
            'bday': 'Дата рождения',
            'biography': 'Биография',
            'prog_langs': 'Любимый язык программирования',
            'sex': 'Пол',
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationModelForm, self).__init__(*args, **kwargs)
        self.fields['prog_langs'].help_text = ''

    def clean_fio(self):
        re_pattern = r'^[\w\sА-Яа-яЁё]+$'
        fio = self.cleaned_data.get('fio').strip()
        if not re.fullmatch(re_pattern, fio):
            raise ValidationError(
                'Fio have only letters',
                code='invalid fio'
            )
        return fio

    def clean_telephone(self):
        re_pattern = r'^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$'
        telephone = self.cleaned_data.get('telephone').strip()
        if not re.fullmatch(re_pattern, telephone):
            raise ValidationError(
                'Telephone have only digits and +, 10 <= digits <= 14',
                code='invalid telephone'
            )
        return telephone

    def clean_email(self):
        re_pattern = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        email = self.cleaned_data.get('email').strip()
        if not re.fullmatch(re_pattern, email):
            raise ValidationError(
                'Invalid email',
                code='invalid email'
            )
        return email

    def clean_bday(self):
        bday = self.cleaned_data.get('bday')
        if not (date(year=1900, month=1, day=1) <= bday <= date.today()):
            raise ValidationError(
                'Invalid birthday',
                code='invalid bday'
            )
        return bday

    def clean_sex(self):
        sex = self.cleaned_data.get('sex').strip()
        if sex not in ('man', 'woman'):
            raise ValidationError(
                'Invalid sex',
                code='invalid sex'
            )
        return sex
