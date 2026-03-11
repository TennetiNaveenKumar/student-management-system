from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# -------------------------
# LOGIN
# -------------------------
def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('/')

    return render(request, 'login.html')


# -------------------------
# LOGOUT
# -------------------------
def logout_user(request):

    logout(request)

    return redirect('/login')


# -------------------------
# STUDENT LIST + PAGINATION
# -------------------------
@login_required
def student_list(request):

    students = Student.objects.all()

    paginator = Paginator(students, 5)   # 5 students per page

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'student_list.html', {'page_obj': page_obj})


# -------------------------
# ADD STUDENT
# -------------------------
@login_required
def add_student(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            email=email,
            course=course
        )

        return redirect('/')

    return render(request, 'add_student.html')


# -------------------------
# EDIT STUDENT
# -------------------------
@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']

        student.save()

        return redirect('/')

    return render(request, 'edit_student.html', {'student': student})


# -------------------------
# DELETE STUDENT
# -------------------------
@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/')