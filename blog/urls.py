from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog_list/', views.blog_list, name='blog-list'),
    path('boglanish/', views.contact_page, name='contact'),
    path('haqimda/', views.about_page, name='about'),
    path('loyihalar/', views.projects_page, name='projects'),
    path('maqola/<slug:slug>/', views.blog_detail, name='blog-detail'),
    path('maqola/yarat/', views.blog_create, name='blog-create'),
    path('maqola/<slug:slug>/tahrir/', views.blog_edit, name='blog-edit'),
    path('maqola/<slug:slug>/ochir/', views.blog_delete, name='blog-delete'),
    path('liked/', views.liked_posts, name='liked'),
    path('rss/', views.rss_view, name='rss'),
    path('maqola/<slug:slug>/', views.blog_detail, name='article_detail'),
]