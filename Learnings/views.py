from django.shortcuts import HttpResponse, render
from firstapp.models import Contact

def home(request):
    if request.method == 'GET':
        name = ["Adib","The Noob","Programming Hero"]
    context = {
        'name': name,
    }
    return render(request,"home.html", context)

def second(request):
    return render(request,"second.html")

