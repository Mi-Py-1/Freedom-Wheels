from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'profile_image')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)