from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Students
from .forms import studentForm



# Create your views here.
def index(request):
    return render(request,'students/index.html',{'students':Students.objects.all()})


def view_student(request,id):
    s=Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            new_student = Students(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                course=form.cleaned_data['course'],
                Grade=form.cleaned_data['Grade']
            )

            new_student.save()

            return render(request, 'students/add.html', {'form': studentForm(), 'success': True})

    else:
        form = studentForm()  # Corrected instantiation of the form
        return render(request, 'students/add.html', {'form': form})
    


def edit(request, id):
  if request.method == 'POST':
    student = Students.objects.get(pk=id)
    form = studentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Students.objects.get(pk=id)
    form = studentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })
   


def delete(request,id):
    if request.method=='POST':
     student = Students.objects.get(pk=id)
     student.delete()

    return HttpResponseRedirect(reverse('Index'))
    