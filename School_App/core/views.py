from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView, FormView

from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from .models import Student
from .forms import StudentRegistration, UserSignupForm

# Create your views here.
#* home fn will add new student and show all students data in table format
def home(request):
  # if request.user.is_authenticated:
  #   return HttpResponseRedirect('/students-info/')
  # else :
  return render(request, 'core/index.html',)


#* User Registration 
class UserSignUpView(FormView):
  """
  Creates new user using Django's built-in model 'User' 
  """
  
  template_name = 'core/user_signup.html'
  form_class = UserSignupForm
  redirect_authenticated_user = True

  success_url = reverse_lazy('student_list')

  def form_valid(self, form) -> HttpResponse:
    user = form.save()
    if user is not None :
      login(self.request, user)
    return super(UserSignUpView, self).form_valid(form)
  
  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('student_list')
    
    return super(UserSignUpView, self).get(*args,**kwargs)
  

class UserLoginView(LoginView):
  """
  Login user to their account after successful check of its credentials, else show error msg
  """
  template_name = 'core/user_login.html'
  fields = "__all__"
  redirect_authenticated_user = True

  def get_success_url(self) -> str:
    return reverse_lazy('student_list')

  



def confirm_delete(request, stud_id):
  student = Student.objects.get(pk=stud_id)

  return render(request, 'core/confirm_delete.html', {'student': student})


#* home fn will delete particular student data from Database and show all remaining students data in table format
def delete(request, stud_id):

  student = Student.objects.get(pk=stud_id)
  student.delete()
  # print("Jay Jay Radhe Govind..💥", stud_id)
  return HttpResponseRedirect('/student-info/')

  
def update(request, stud_id):
  student = Student.objects.get(pk=stud_id)
  if request.method == 'POST':
    form = StudentRegistration(request.POST, instance=student)
    if form.is_valid():
      nm = form.cleaned_data['name']
      em = form.cleaned_data['email']
      pswd = form.cleaned_data['password']
      student = Student(id=stud_id, name=nm, email=em, password=pswd)
      student.save()
      # print(nm, em, pswd, 'Shree Dnyanoba Mauli Tukaram...✨')
  else:
    form = StudentRegistration(instance=student)
    # print("Jay Shree Ram Krushna Hari ...🙏🏻")
  
  return render(request, 'core/update.html', context={'form': form, })


#* student info view shows students list
class StudentsInfoView(ListView):
  model = Student
  context_object_name = 'students'
  template_name = 'core/students_info.html'
  # ordering = ['-name']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class StudentRegistrationView(CreateView):
  template_name = 'core/student_registration.html'
  model = Student
  fields = '__all__'
  url = '/'
  # form = StudentRegistration

def student_registration(request):
  if request.method == 'POST':
    form = StudentRegistration(request.POST)
    if form.is_valid():
      stud_name = form.cleaned_data['name']
      stud_email = form.cleaned_data['email']
      pswd = form.cleaned_data['password']
      student = Student.objects.create(name=stud_name, email=stud_email, password=pswd)
      student.save()
      messages.success(request, f"Registration of {stud_name} as student is successful. ✨")
      return HttpResponseRedirect('/student-create/')
  else:
    form = StudentRegistration()
  
  return render(request, 'core/student_registration.html', {'form': form})
