from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import ProfileForm, PostForm, ContactForm
from .models import Profile, Post
from django.core.mail import send_mail
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def whycyclingcanhelp(request):
    return render(request, 'whycyclingcanhelp.html')

def servicesavailable(request):
    return render(request, 'servicesavailable.html')

def helpus(request):
    return render(request, 'helpus.html')

def community(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    return render(request, 'community.html', {'profiles': profiles, 'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # Get the superuser email
            superuser_email = User.objects.filter(is_superuser=True).first().email

            # Send email to superuser
            send_mail(
                subject=f"Contact Us Message from {first_name} {last_name}",
                message=f"Message: {message}\n\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}",
                from_email=email,
                recipient_list=[superuser_email],
            )

            # Redirect to the same page with a success flag
            return redirect(f'{request.path}?success=true')
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_edit')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def profile(request, user_id):
    user_profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, 'profile.html', {'profile': user_profile})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_detail(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile_detail.html', {'profile': user_profile})

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {'form': form})

def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('account_deleted')
    return render(request, 'profile_delete_confirm.html')

def account_deleted(request):
    return render(request, 'account_deleted.html')

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

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post_confirm.html', {'post': post})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})