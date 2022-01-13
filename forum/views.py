from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Solution



def homePage(request):
    posts = Post.objects.all
    
    print(posts)
    context = {'posts': posts}
    return render(request, 'forum/home.html', context)


def solutionPage(request, pk, ck):
    solutions = Solution.objects.filter(post__id=pk)
    print(solutions)
    context = {'solutions': solutions}
    return render(request, 'forum/solution.html', context)

    