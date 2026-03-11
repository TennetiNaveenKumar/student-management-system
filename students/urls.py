from django.urls import path
from . import views

urlpatterns = [

path('', views.student_list),

path('login/', views.login_user),

path('logout/', views.logout_user),

path('add/', views.add_student),

path('edit/<int:id>/', views.edit_student),

path('delete/<int:id>/', views.delete_student),

]