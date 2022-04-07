from importlib.resources import contents
from operator import contains
from django import forms

#declearinng the form class
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label="Your Name")
    phone=forms.CharField(max_length=100,label="Your Phone")
    contact=forms.CharField(max_length=100,label="Your Description")
    