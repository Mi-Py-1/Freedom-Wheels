from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
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
    if request.user.is_authenticated:
        posts = Post.objects.all()
        profiles = Profile.objects.all()
        return render(request, 'community.html', {'posts': posts, 'profiles': profiles})
    else:
        form = AuthenticationForm()
        return render(request, 'community.html', {'form': form})

def contactus(request):
    return render(request, 'contactus.html')

def loginregister(request):
    return render(request, 'loginregister.html')

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author__profile__in=request.user.profile.follows.all()).order_by('-created_at')
    else:
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

@login_required
def profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, 'profile.html', {'profile': profile})

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
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

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

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})