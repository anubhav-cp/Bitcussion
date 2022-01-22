from cgi import print_environ
import imp
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Post, Solution
from .forms import postForm, solutionForm
from django.contrib.auth.decorators import login_required



def homePage(request):
    posts = Post.objects.all

    active_posts = Post.objects.filter(isactive = True)[:5]

    print(active_posts)

    print(posts)
    context = {'posts': posts, 'active_posts': active_posts}
    return render(request, 'forum/home.html', context)


def solutionPage(request, pk, ck):
    

    posts = Post.objects.get(id=pk)
    forms = solutionForm()
    solutions = Solution.objects.filter(post__id=pk)
    print(solutions)

    
    if request.method == 'POST':
        forms = solutionForm(request.POST)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.post = posts
            data.profile = request.user.userprofile
            forms.save()


    context = {'solutions': solutions, 'posts': posts, 'forms': forms}
    return render(request, 'forum/solution.html', context)


@login_required(login_url='login')
def createPost(request):
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile = request.user.userprofile
            form.save()

            return redirect('home')


    context = {'form': form}
    return render(request, 'forum/createPost.html', context)


# def createSoltuion(request):
#     forms = solutionForm()

#     context = {'forms': forms}
#     return render(request, 'forum/solution.html', context)
    