from django import forms
from django.forms.models import ModelForm


class quoteForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    details = forms.CharField(widget=forms.Textarea)

    def check_spam(self):
        common_spam_keywords = ["href", "https", "click", "http", "www", "//"]

        if self.cleaned_data['details'] is not None:
            for keyword in common_spam_keywords:
                if keyword in self.cleaned_data['details'].lower():
                   return 1
            return self.cleaned_data
