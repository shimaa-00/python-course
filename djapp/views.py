from contextlib import redirect_stdout
from multiprocessing import context
from django.shortcuts import render,redirect

from djapp.serializers import StudentSerializer
from .models import Student,Track
from .forms import StudentForm
from rest_framework.response import Response

from rest_framework.decorators import api_view
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
@api_view(['GET'])
def api_all_students(request):
    all_students =Student.objects.all()
    student_serializer = StudentSerializer(all_students , many = True)
    return Response(student_serializer.data)

@api_view(['GET'])
def api_one_student(request,student_id):
    student = Student.objects.get(id = student_id)
    student_serializer = StudentSerializer(student, many = False)
    return Response(student_serializer.data)


@api_view(['POST'])

def api_add_student(request):
    student_serializer = StudentSerializer(data=request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return redirect('api-all') 
     
@api_view(['POST'])
def api_edit_student(request,student_id):
    student = Student.objects.get(id = student_id)
    student_serializer = StudentSerializer(data = request.data ,instance=student)
    if student_serializer.is_valid():
        student_serializer.save()
        return redirect('api-all')
@api_view(['DELETE'])
def api_delete_student(request,student_id):
    student = Student.objects.get(id = student_id) 
    student.delete()
    return Response('Student deleted')

 