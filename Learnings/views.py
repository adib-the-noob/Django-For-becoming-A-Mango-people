from multiprocessing import context
from django.shortcuts import HttpResponse, render

def home(request):
    name = ["Adib","The Noob","Programming Hero"]
    context = {
        'name': name,
    }
    return render(request,"home.html", context)