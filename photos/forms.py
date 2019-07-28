from django import forms
from .models import Image,Profile

class photoForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Likes', 'profile']
       

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']




