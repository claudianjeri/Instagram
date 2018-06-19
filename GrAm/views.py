from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment
from .forms import EditProfileForm, UploadForm
# Create your views here.
def start(request):

   return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
def home(request):
    image = Image.get_images()
    return render(request, 'base.html', {"images":image})

def signin(request):
    print('hey')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')

    else:
        form = UserCreationForm()

        args = {"form": form} 

        return render(request, 'registration/registration_form.html', args) 

def login(request):

    return render(request, 'registration/login.html')

def profile(request):
    profile = Profile.get_profile()
    image = Image.get_images()
    user = get_object_or_404(User, pk=pk)
    return render(request, 'profile/profile.html', {"profile":profile, "images":image, "user":user})

def update(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request,'profile/edit.html',{"form":form})

def upload(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = UploadForm()
            return render(request,'upload.html',{"user":current_user,
                                                    "form":form})