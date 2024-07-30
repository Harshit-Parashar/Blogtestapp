from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

# class BlogForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField() 
    

#we will see use of Django-ModelForms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['description', 'photo']



class UserRegistrationForm(UserCreationForm):
    #adding 1 more field to UserCreation form i.e. email
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



