from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileForm
from .models import Post, Profile

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def whyclingcanhelp(request):
    return render(request, 'whyclingcanhelp.html')

def servicesavailable(request):
    return render(request, 'servicesavailable.html')

def helpus(request):
    return render(request, 'helpus.html')

def community(request):
    return render(request, 'community.html')

def contactus(request):
    return render(request, 'contactus.html')

def loginregister(request):
    return render(request, 'loginregister.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})