from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import HttpResponse, render

def home(request):
    if request.method == 'GET':
        name = ["Adib","The Noob","Programming Hero"]
    context = {
        'name': name,
    }
    return render(request,"home.html", context)

def second(request):
    return render(request,"second.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        print("Submitted name is ",name)
        print("Submitted Phone is ",phone)
        print("Submitted Description is ",content) 
    return render(request,"contact.html")