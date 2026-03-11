from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)