from django.shortcuts import render
from .models import Contact
import requests
import json


def index(request):
    if request.method == "POST":
        first_name   = request.POST.get('firstname')
        last_name    = request.POST.get('lastname')
        
        r = requests.get("http://api.icndb.com/jokes/random?firstName=" + first_name + "&;lastName=" + last_name)
        json_data = json.loads(r.text)

        joke = json_data.get('value').get('joke')

        context = {'joker' : joke}

        return render(request, 'mysite/index.html', context)
    else:
        return render(request, 'mysite/index.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def contact(request):
    if request.method == "POST":
        email   = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(email = email, subject = subject, message = message)
        c.save()

        return render(request, 'mysite/contact.html')
    else:
        return render(request, 'mysite/contact.html')

