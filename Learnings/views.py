from django.shortcuts import HttpResponse, render

def home(request):
    return render(request,"home.html")