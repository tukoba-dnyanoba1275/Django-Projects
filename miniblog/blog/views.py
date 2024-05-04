from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import  UserChangeForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib import messages

from .forms import UserSignupForm, UserLoginForm, PostEditForm
from .models import Post

#* Home
def home(request):
  posts = Post.objects.all()
  return render(request, 'blog/home.html', context={'home': 'selected', 'posts': posts})

#* About
def about(request):
  return render(request, 'blog/about.html', context={'about': 'selected'})

#* Contact
def contact(request):
  return render(request, 'blog/contact.html', context={'contact': 'selected'})

#* Signup
def user_signup(request):
  if request.method == 'POST':
    form = UserSignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      group = Group.objects.get(name='Author')
      user.groups.add(group)
      messages.success(request, "Congratulations!! You have become an AUTHOR.")
      messages.info(request, "Now, you can login.")
      return HttpResponseRedirect('/login/')
  else:
    form = UserSignupForm()
  return render(request, 'blog/signup.html', context={'signup': 'selected', 'form': form})


#* login
def user_login(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect('/dashboard/')
  else:
    if request.method == 'POST':
      # form = AuthenticationForm(request=request, data=request.POST)
      form = UserLoginForm(request=request, data=request.POST)
      if form.is_valid():
        nm = form.cleaned_data['username']
        pswd = form.cleaned_data['password']
        user_obj = authenticate(username=nm, password=pswd)
        if user_obj is not None:
          login(request, user_obj)
          messages.success(request, "Logged in SUCCESSFULLY !!")
          return HttpResponseRedirect('/dashboard/')
    else:
      # form = AuthenticationForm()
      form = UserLoginForm()
    return render(request, 'blog/login.html', context={'login': 'selected', 'form': form})

#* logout
def user_logout(request):
  logout(request)
  messages.success(request, "Logged off successfully...!!")
  return HttpResponseRedirect('/login/')

#* dashboard
def dashboard(request):
  if request.user.is_authenticated:
    posts = Post.objects.all()
    user = request.user
    full_name = user.get_full_name()
    grps = user.groups.all()
    return render(
      request, 'blog/dashboard.html',
      context={'dashboard': 'selected', 'posts': posts, 'full_name': full_name, 'groups':grps}
    )
  else:
   return HttpResponseRedirect('/login/')
  

#* add post from Dashboard
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = PostEditForm(request.POST)
      if form.is_valid():
        titl = form.cleaned_data['title']
        desc = form.cleaned_data['description']
        Post(title=titl, description=desc)
        form.save()
        messages.success(request, "Post added SUCCESSFULLY !!")
        return HttpResponseRedirect('/dashboard/')
    else:
      form = PostEditForm()
    return render(request, 'blog/add_edit_post.html', {'form': form, 'add_post': True})
  else:
    return HttpResponseRedirect('/login/')


#* edit/update post from Dashboard
def edit_post(request, post_id):
  if request.user.is_authenticated:
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
      form = PostEditForm(request.POST, instance=post)
      if form.is_valid():
        form.save()
        messages.success(request, "Post updated SUCCESSFULLY !!")
        return HttpResponseRedirect('/dashboard/')
    else:
      form = PostEditForm(instance=post)
    return render(request, 'blog/add_edit_post.html', {'form': form, 'add_post': False})
  else:
    return HttpResponseRedirect('/login/')


#* delete post from Dashboard
def delete_post(request, post_id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      post = Post.objects.get(pk=post_id)
      post.delete()
      messages.warning(request, f"Post having title {post_id} is  deleted")
      return HttpResponseRedirect('/dashboard/')
    
  else:
    return HttpResponseRedirect('/login/')



# #* setting cookies
# def setcookie(request):
#   return render(request, 'blog')