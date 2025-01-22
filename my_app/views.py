from django.shortcuts import render
from .models import Post

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