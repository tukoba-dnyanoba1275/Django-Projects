from django import forms
from .models import Student

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