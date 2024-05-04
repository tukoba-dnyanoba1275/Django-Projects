from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('add_post/', views.add_post, name='add_post'),
  path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
  path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]