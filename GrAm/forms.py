from .models import Image, Profile, Comment
from django import forms
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']