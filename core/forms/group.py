# -*- coding: utf-8 -*-
from django import forms
from core.models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group

        fields = [
            'name',
            'professor_guide',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'professor_guide': forms.Select(attrs={'class': 'form-control'}),
        }
