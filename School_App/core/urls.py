from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.UserSignUpView.as_view(), name='user_signup'),
  path('login/', views.UserLoginView.as_view(), name='user_login'),
  path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
  path('update/<int:stud_id>/', views.update, name='update'),
  path('confirm-delete/<int:stud_id>/', views.confirm_delete, name='confirm_delete'),
  path('<int:stud_id>/', views.delete, name='delete'),
  path('students-info/', views.StudentsInfoView.as_view(), name='student_list'),
  # path('student-create/', views.StudentRegistrationView.as_view(), name='register_student'),
  path('student-create/', views.student_registration, name='register_student'),
]