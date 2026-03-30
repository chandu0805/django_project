
from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
