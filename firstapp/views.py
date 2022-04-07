from django.shortcuts import render
# Create your views here.
from django.contrib import admin
from django.urls import path
from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['contact']
            
        #creating Object of Contact
        obj = Contact(name=name, phone=phone, content=content)
        obj.save()
    else:
        form=ContactForm()
    
    return render(request,"contact.html",{'form':form})
