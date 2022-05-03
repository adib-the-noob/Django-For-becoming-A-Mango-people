from tkinter.ttk import Widget
from django import forms
from .models import Contact, Post

#declearinng the form class
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields='__all__'
        
class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        exclude=['created_at','slug','id','user']
        widget={
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True}),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True})}