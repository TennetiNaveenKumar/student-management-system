from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# -------------------------
# LOGIN
# -------------------------
def login_user(request):
    # support ?next=/some/path redirect after login
    next_url = request.GET.get('next') or request.POST.get('next')

    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect to next_url if provided else home
            return redirect(next_url or '/')
        else:
            error = "Invalid username or password."

    return render(request, 'students/login.html', {'error': error, 'next': next_url})


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

    return render(request, 'students/student_list.html', {'page_obj': page_obj})


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

    return render(request, 'students/add_student.html')


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

    return render(request, 'students/edit_student.html', {'student': student})


# -------------------------
# DELETE STUDENT
# -------------------------
@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/')