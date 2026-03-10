from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        # use .get() to avoid MultiValueDictKeyError and validate inputs
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        age = request.POST.get('age')

        if not age:
            # re‑render form with an error message
            error = "Age is required."
            return render(request, 'students/add.html', {'error': error,
                                                          'name': name,
                                                          'email': email,
                                                          'course': course})

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
