from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def start(request):

   return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
def home(request):

    return render(request, 'base.html')

def signin(request):

    return render(request, 'registration/signup.html')

def login(request):

    return render(request, 'registration/login.html')

def profile(request):

    return render(request, 'profile.html')

