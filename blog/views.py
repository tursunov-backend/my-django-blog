from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')

def blog_list(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='blog_list.html')

def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='contact.html')

def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')

def projects_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='projects.html')

def blog_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request=request, template_name='blog_detail.html')

def blog_create(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='blog_create.html')

def blog_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request=request, template_name='blog_edit.html')

def blog_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request=request, template_name='blog_delete.html')