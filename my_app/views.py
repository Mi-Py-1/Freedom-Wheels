from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm, PostForm
from .models import Post, Profile

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def whycyclingcanhelp(request):  # Corrected function name
    return render(request, 'whycyclingcanhelp.html')

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
    posts = Post.objects.all().order_by('-created_at')
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

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile_detail.html', {'profile': profile})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    request.user.profile.follows.add(user_to_follow.profile)
    return redirect('profile_detail', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    request.user.profile.follows.remove(user_to_unfollow.profile)
    return redirect('profile_detail', username=username)