from django.contrib import admin
from .models import Student

admin.site.register(Student)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'classroom', 'gender', 'academic', 'status', 'score']