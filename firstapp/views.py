from django.shortcuts import render
from firstapp.models import Post
# Create your views here.

from .forms import ContactForm,PostForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()
    
    return render(request,"contact.html",{'form':form})

def PostView(request):
    post = Post.objects.all()
    return render(request,'firstapp/postview.html',{'post': post})

def postcreate(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.user = request.user
    else:
        form = PostForm()
    return render(request,'firstapp/postcreate.html',{'form':form})