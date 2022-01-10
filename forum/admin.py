from django.contrib import admin
from django.http.request import split_domain_port
from .models import Post, Tag, Solution

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Solution)
