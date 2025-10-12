from django.shortcuts import render
from .models import Student

# Create your views here.
def student_List(request):
    student = Student.objects.all()
    return render(request, 'students/student_list.html', {'student': student})


