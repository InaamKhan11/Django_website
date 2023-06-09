import datetime
from email import message
from importlib.resources import contents
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse
from importlib_metadata import email
from datetime import datetime
from django.contrib import messages


from pyparsing import Combine
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    # messages.success(request,"this is my message")
    return render(request, 'index.html', context)
    # return HttpResponse("this is a homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is a about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is a services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request,"Your message has been send")
    return render(request, 'contact.html')
    # return HttpResponse("this is a contact page")


