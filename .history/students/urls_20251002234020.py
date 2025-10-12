from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add', views.add_student, name='add_student'), # Add this line to map the URL to the add_student view
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'), 
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),    
]
