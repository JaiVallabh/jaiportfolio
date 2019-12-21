from django.shortcuts import render
from .models import Cert
def home(request):
    certs=Cert.objects
    return render(request,'certifications/home.html',{'certs':certs})
