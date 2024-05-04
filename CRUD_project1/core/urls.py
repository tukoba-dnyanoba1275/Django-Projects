from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('update/<int:stud_id>/', views.update, name='update'),
  path('confirm-delete/<int:stud_id>/', views.confirm_delete, name='confirm_delete'),
  path('<int:stud_id>/', views.delete, name='delete'),
]