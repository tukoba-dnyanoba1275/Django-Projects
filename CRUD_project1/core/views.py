from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Student
from .form import StudentRegistration

# Create your views here.
#* home fn will add new student and show all students data in table format
def home(request):
  if request.method == 'POST':
    form = StudentRegistration(request.POST)
    if form.is_valid():
      nm = form.cleaned_data['name']
      em = form.cleaned_data['email']
      pswd = form.cleaned_data['password']
      student = Student(name=nm, email=em, password=pswd)
      student.save()
      # form = StudentRegistration()
      return HttpResponseRedirect('/')
  else:
    form = StudentRegistration()
  
  students = Student.objects.all()
  
  return render(request, 'core/index.html', context={'form': form, 'students': students})


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




class StudentsInfoView(ListView):
  model = Student
  context_object_name = 'students'
  template_name = 'core/students_info.html'
  # ordering = ['-name']


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
