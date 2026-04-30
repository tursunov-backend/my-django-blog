from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .db import Database


db = Database()


def home_page(request: HttpRequest) -> HttpResponse:
    articles = db.get_latest_articles()
    return render(request=request, template_name='home.html', context={'articles': articles})


def articles_page(request: HttpRequest) -> HttpResponse:
    articles = db.get_articles()
    return render(request=request, template_name='articles.html', context={'articles': articles})


def article_details_page(request: HttpRequest, slug: str) -> HttpResponse:
    article = db.get_article_by_slug(slug)
    return render(request=request, template_name='details.html', context={'article': article})


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')


def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='contact.html')