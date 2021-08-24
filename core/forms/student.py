# -*- coding: utf-8 -*-
from django import forms
from core.models import Student
from django.utils.translation import gettext_lazy as _


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'age',
            'gender',
            'email',
            'date_birthday',
            'city_birthday',
            'group',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'age': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'return isNumber(event);'}),

            'gender': forms.Select(attrs={'class': 'form-control'}),

            'email': forms.TextInput(attrs={'class': 'form-control'}),

            'group': forms.Select(attrs={'class': 'form-control'}),
        }

    date_birthday = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control datetime', 'readonly': True, 'required': True}),
        label=_('date birthday').capitalize()
    )

    city_birthday = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control datetime', 'readonly': True, 'required': True}),
        label=_('city birth').capitalize()
    )

    def clean_age(self):
        age = self.cleaned_data['age']
        if 15 > age or age > 35:
            raise forms.ValidationError(_('Please enter an age between 15 and 35.'))
        return age
