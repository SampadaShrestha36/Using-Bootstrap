from django.shortcuts import render
from .models import Contacts
# Create your views here.
def home(request):
    return render(request,'home.html')
def submit(request):
    if request.method=='POST':
        data=request.POST
        name=data['name']
        email=data['email']
        contactno=data['contactno']
        message=data['message']

        user=Contacts(name=name,email=email,contactno=contactno,message=message)
        user.save()
        return render(request,'submit.html')