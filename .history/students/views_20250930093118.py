from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request): 
    query = request.GET.get('q')  # Lấy giá trị của tham số 'q' từ URL
    if query:  # Nếu có tham số 'q', lọc danh sách học sinh theo tên
        students = Student.objects.filter(name__icontains=query) # Sử dụng icontains để tìm kiếm không phân biệt chữ hoa chữ thường
    else:  # Nếu không có tham số 'q', hiển thị tất cả học sinh
        students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) # StudentForm là một lớp biểu mẫu được định nghĩa trong forms.py
        if form.is_valid(): # Kiểm tra tính hợp lệ của dữ liệu biểu mẫu
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm() # Tạo một biểu mẫu trống để hiển thị trên trang web
    return render(request, 'students/add_student.html', {'form': form}) # Truyền biểu mẫu vào ngữ cảnh để hiển thị trong template

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id) # Lấy đối tượng Student theo ID hoặc trả về lỗi 404 nếu không tìm thấy
    return render(request, 'students/student_detail.html', {'student': student})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student) # instance=student để cập nhật đối tượng hiện có
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student) # Tạo biểu mẫu với dữ liệu hiện có của học sinh
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})

# Hàm xử lý tìm kiếm học sinh theo tên
# def search_students(request):
#     query = request.GET.get('q')  # Lấy giá trị của tham số
#     if query:
#         students = Student.objects.filter(name__icontains=query) # Sử dụng icontains để tìm kiếm không phân biệt chữ hoa chữ thường
#     else: # Nếu không có tham số 'q', hiển thị tất cả học sinh                
#         students = Student.objects.all()
#     return render(request, 'students/student_list.html', {'students': students})
#     return render(request, 'students/student_list.html', {'students': students})
#     return render(request, 'students/student_list.html', {'students': students})