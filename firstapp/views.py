from django.shortcuts import render

from firstapp.models import Post
# Create your views here.

from .forms import ContactForm

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
