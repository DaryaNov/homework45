from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class ArticleForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    maxdescription = forms.CharField(max_length=3000, required=True, label='Подробное описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    date_completion = forms.CharField(max_length=10, required=False, label='Дата выполнения')