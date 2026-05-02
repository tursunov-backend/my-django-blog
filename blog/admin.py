# blog/admin.py
from .models import Article
from django.contrib import admin

admin.site.register(Article)