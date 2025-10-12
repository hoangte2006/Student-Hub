from django.contrib import admin
from .models import Student

@admin.register(Student) # Đăng ký mô hình Student với trang quản trị Django 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'classroom', 'gender', 'academic', 'status', 'score']
