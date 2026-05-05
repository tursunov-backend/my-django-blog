from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .db import Database
from django.http import Http404
from .forms import GetArticleQueryForm

db = Database()

def home_page(request: HttpRequest) -> HttpResponse:
    page = int(request.GET.get('page', 1))
    per_page = 3
    all_articles = db.get_articles()

    start = (page - 1) * per_page
    end = start + per_page
    articles = all_articles[start:end]
    total_pages = (len(all_articles) + per_page - 1) // per_page

    return render(request=request, template_name='home.html', context={
        'articles': articles,
        'page': page,
        'total_pages': total_pages,
        'has_next': page < total_pages,
        'has_prev': page > 1,
    })
def blog_list(request: HttpRequest) -> HttpResponse:
    form = GetArticleQueryForm(request.GET)
    
    if form.is_valid():
        data = form.cleaned_data

        articles = db.get_articles_by_title(data['search'])

        
        return render(request=request, template_name='blog_list.html', context={'articles': articles})
    articles = db.get_articles
    return render(request=request, template_name='blog_list.html', context={'articles': articles, 'form': form})


def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
    article = db.get_article_by_slug(slug)
    if article is None:
        raise Http404
    return render(request, 'blog_detail.html', {'article': article})

def contact_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        errors = []
        if not name:    errors.append("Ism kiritilmadi.")
        if not email:   errors.append("Email kiritilmadi.")
        if not message: errors.append("Xabar kiritilmadi.")

        if errors:
            return render(request, 'contact.html', {'errors': errors})
        return redirect('home')

    return render(request=request, template_name='contact.html')

def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')

def projects_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='projects.html')

def blog_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        title   = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        errors = []
        if not title:   errors.append("Sarlavha kiritilmadi.")
        if not content: errors.append("Matn kiritilmadi.")

        if errors:
            return render(request, 'blog_create.html', {'errors': errors})
        return redirect('home')

    return render(request=request, template_name='blog_create.html')

def blog_edit(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        title   = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        errors = []
        if not title:   errors.append("Sarlavha kiritilmadi.")
        if not content: errors.append("Matn kiritilmadi.")

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

def articles_page(request: HttpRequest) -> HttpResponse:
    articles = db.get_articles()
    return render(request=request, template_name='articles.html', context={'articles': articles})

def article_detail_page(request: HttpRequest, slug: str) -> HttpResponse:
    article = db.get_article_by_slug(slug)
    return render(request=request, template_name='detailes.html', context={'article': article})

def rss_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("RSS page")