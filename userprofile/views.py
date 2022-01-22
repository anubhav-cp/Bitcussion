from operator import methodcaller
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import customUserCreationForm


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'userprofile/login.html')


def logoutPage(request):
        logout(request)

        return redirect('login')


def registerPage(request):
    form = customUserCreationForm()
    
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')



    context = {'form': form}
    return render(request, 'userprofile/register.html', context)
