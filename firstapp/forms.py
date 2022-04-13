from dataclasses import field
from django import forms
from .models import Contact

#declearinng the form class
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields='__all__'