from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _

from .models import Post


#* Signup Form
class UserSignupForm(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput())
  class Meta():
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    labels = {
      'first_name': 'First Name',
      'lasst_name': 'Last Name',
      'email': 'Email',
    }
    widgets = {
      'username': forms.TextInput(attrs={'placeholder': 'kv_yadav21'}),
      'first_name': forms.TextInput(attrs={'placeholder': 'Shree Krushna'}),
      'last_name': forms.TextInput(attrs={'placeholder': 'Yadav'}),
      'email': forms.EmailInput(attrs={'placeholder': 'krushn21yadav@gmail.com', 'required':''}),
    }



class UserLoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your username here...'}))
  password = forms.CharField(
    label=_("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': 'Enter Your Password here...'}),
  )

#* to edit post with ModelForm
class PostEditForm(forms.ModelForm):
  class Meta():
    model = Post
    fields = ('title', 'description')
    # labels = {'title'}
    widgets = {
      'title': forms.TextInput(attrs={'placeholder': 'Enter Post Title here....'}),
      'description': forms.Textarea(attrs={'placeholder': 'Enter Description of Post here....'}),
    }