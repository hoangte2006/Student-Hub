from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect

# Create your views here.
def student_list(request): #
    student = Student.objects.all()
    return render(request, 'students/student_list.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) # StudentForm là một lớp biểu mẫu được định nghĩa trong forms.py
        if form.is_valid(): # Kiểm tra tính hợp lệ của dữ liệu biểu mẫu
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})
