from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('undo-delete/', views.undo_delete, name='undo_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('trash/', views.trash_list, name='trash_list'),  # Danh sách học sinh đã xoá
    path('restore/<int:student_id>/', views.restore_student, name='restore_student'),  # Khôi phục học sinh từ thùng rác
    path('delete-forever/<int:student_id>/', views.delete_forever, name='delete_forever'),  # Xoá vĩnh viễn học sinh

]
