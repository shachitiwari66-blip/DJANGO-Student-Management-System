from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),   # HOME PAGE
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/add/', views.add_student, name='add_student'),
     path('student/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path("students/", views.students_page, name="students_page"),
    
]

