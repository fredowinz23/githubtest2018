from django.shortcuts import render
from .models import Contact
# Create your views here.

def view(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/index.html',{'contact_list':contact_list})
