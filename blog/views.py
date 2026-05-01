from django.shortcuts import render
from django.http import  HttpRequest, HttpResponse

def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')

def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='contact.html')