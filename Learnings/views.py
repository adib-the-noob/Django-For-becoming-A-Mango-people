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

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        
        #creating Object of Contact
        obj = Contact(name=name, phone=phone, content=content)
        obj.save()
        
    return render(request,"contact.html")