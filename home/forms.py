from django import forms
from django.forms.models import ModelForm


class quoteForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    details = forms.CharField(widget=forms.Textarea)
