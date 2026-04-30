from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('articles/', views.articles_page, name='articles'),
    path('articles/<slug:slug>/', views.article_details_page, name='article_details'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]