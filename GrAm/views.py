from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image, Profile

# Create your views here.
def start(request):

   return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
def home(request):
    image = Image.objects.all()
    return render(request, 'base.html', {"images":image})

def signin(request):
    
    return render(request, 'registration/signup.html')

def login(request):

    return render(request, 'registration/login.html')

def profile(request):
    profile = Profile.objects.all()
    return render(request, 'profile/profile.html', {"profile":profile})

