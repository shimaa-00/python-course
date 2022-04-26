from contextlib import redirect_stdout
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Student,Track
from .forms import StudentForm
# Create your views here.
def home (request):
    all_students=Student.objects.all()
    context={"all_students":all_students}
    return render(request , 'djapp/home.html',context)
def show (request,student_id):
    student = Student.objects.get(id = student_id)
    context = {'student':student}
    return render(request,'djapp/show.html',context)
    pass
def delete(request,student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect('home')
def addStudent(request):
    st_form=StudentForm()
    if request.method == 'POST':
        st_form=StudentForm(request.POST)
        if st_form.is_valid:
            st_form.save()
            return redirect('home')

    context={'st_form':st_form}
    return render(request,'djapp/add.html',context)
def editStudent(request,student_id):
    student = Student.objects.get(id = student_id)
    st_form = StudentForm(instance=student)
    if request.method == 'POST':
        st_form=StudentForm(request.POST,instance=student)
        if st_form.is_valid:
            st_form.save()
            return redirect('home')
    context ={'st_form':st_form}
    return render(request ,'djapp/add.html',context)