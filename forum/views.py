from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Solution
from .forms import postForm, solutionForm



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

    
    if request.method == 'POST':
        forms = solutionForm(request.POST)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.post = posts
            forms.save()


    context = {'solutions': solutions, 'posts': posts, 'forms': forms}
    return render(request, 'forum/solution.html', context)


def createPost(request):
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form}
    return render(request, 'forum/createPost.html', context)


# def createSoltuion(request):
#     forms = solutionForm()

#     context = {'forms': forms}
#     return render(request, 'forum/solution.html', context)
    