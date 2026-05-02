from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse

from .db import Database

db = Database()

def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')


def blog_list(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='blog_list.html')


def contact_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Oddiy validatsiya
        errors = []
        if not name:
            errors.append("Ism kiritilmadi.")
        if not email:
            errors.append("Email kiritilmadi.")
        if not message:
            errors.append("Xabar kiritilmadi.")

        if errors:
            return render(request, 'contact.html', {'errors': errors})

        # Muvaffaqiyatli yuborildi — hozircha home ga redirect
        return redirect('home')

    return render(request=request, template_name='contact.html')


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')


def projects_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='projects.html')


def blog_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request=request, template_name='blog_detail.html')


def blog_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        title   = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        errors = []
        if not title:
            errors.append("Sarlavha kiritilmadi.")
        if not content:
            errors.append("Matn kiritilmadi.")

        if errors:
            return render(request, 'blog_create.html', {'errors': errors})

        return redirect('home')

    return render(request=request, template_name='blog_create.html')


def blog_edit(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        title   = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        errors = []
        if not title:
            errors.append("Sarlavha kiritilmadi.")
        if not content:
            errors.append("Matn kiritilmadi.")

        if errors:
            return render(request, 'blog_edit.html', {'errors': errors, 'pk': pk})

        return redirect('home')

    return render(request=request, template_name='blog_edit.html')


def blog_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        return redirect('home')

    return render(request=request, template_name='blog_delete.html')


def liked_posts(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='liked.html')


def blog_list(request):
    articles = db.get_articles()
    return render(request, 'blog_list.html', {'articles': articles})


def blog_detail(request, slug):
    article = db.get_article_by_slug(slug)
    return render(request, 'blog_detail.html', {'article': article})