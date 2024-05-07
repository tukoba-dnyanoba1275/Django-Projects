from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class UserSignupForm(UserCreationForm):
  email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder':'example951@email.com'}))
  first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Shyam'}))
  last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Patil'}))
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    labels = {}
    error_messages = {}
    widgets = {
      'username': forms.TextInput(attrs={'placeholder':'shyam_p25'}),
      'password1': forms.PasswordInput(attrs={'placeholder':'Madhav@$852!'}),
    }



class StudentRegistration(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name', 'email', 'password']
    error_messages = {
      'name': {'required':'Enter Your Full Name !'},
      'email': {'required':'Enter Your Email !'},
      'password': {'required':'Enter Your Password !'},
    }

    widgets = {
      'password': forms.PasswordInput()
    }