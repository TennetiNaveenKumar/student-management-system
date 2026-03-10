from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            email=email,
            course=course,
            age=age
        )
    
        return redirect('student_list')

    return render(request, 'students/add.html')

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')
