from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post



def homePage(request):
    posts = Post.objects.all
    
    print(posts)
    context = {'posts': posts}
    return render(request, 'forum/home.html', context)

    