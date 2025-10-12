from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add', views.add_student, name='add_student'), # Add this line to map the URL to the add_student view
    path('<int:student_id>/', views.student_detail, name='student_detail') #` Add this line to map the URL to the student_detail view`
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'), # Add this line to map the URL to the edit_student view
    path('delete/<int:student_id>/', views.delete_student, name='delete_student
]
