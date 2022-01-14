from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Solution
from .forms import postForm



def homePage(request):
    posts = Post.objects.all

    print(posts)
    context = {'posts': posts}
    return render(request, 'forum/home.html', context)


def solutionPage(request, pk, ck):
    posts = Post.objects.get(id=pk)
    solutions = Solution.objects.filter(post__id=pk)
    print(solutions)
    context = {'solutions': solutions, 'posts': posts}
    return render(request, 'forum/solution.html', context)


def createPost(request):
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form}
    return render(request, 'forum/createPost.html', context)

    