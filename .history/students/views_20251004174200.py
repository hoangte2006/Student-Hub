from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Avg    
from django.contrib import messages 


# Create your views here.

def home(request):
    return render(request, 'students/home.html')

def student_list(request): 
    classroom = request.GET.get('classroom') # Lấy giá trị của tham số 'classroom' từ URL (nếu có)
    gender = request.GET.get('gender') # Lấy giá trị của tham số 'gender' từ URL (nếu có)
    status = request.GET.get('status') # Lấy giá trị của tham số 'status' từ URL (nếu có) 
    students = Student.objects.all() # Lấy tất cả đối tượng Student từ cơ sở dữ liệu

    if classroom: # Nếu có tham số 'classroom' trong URL, lọc danh sách học sinh theo lớp
        students = students.filter(classroom__icontains=classroom) # __icontains: lọc không phân biệt chữ hoa chữ thường    
    if gender:
        students = students.filter(gender__icontains=gender)
    if status:
        students = students.filter(status__icontains=status)
    
    return render(request, 'students/student_list.html',{
        'students': students,
        'classroom': classroom,
        'gender': gender,
        'status': status,
    })
                  
def add_student(request):
    if request.method == 'POST':# Nếu biểu mẫu được gửi đi
        form = StudentForm(request.POST) # StudentForm là một lớp biểu mẫu được định nghĩa trong forms.py
        if form.is_valid(): # Kiểm tra tính hợp lệ của dữ liệu biểu mẫu
            form.save()
            messages.success(request, 'Thêm học sinh thành công!')
            return redirect('student_list')
    else:
        form = StudentForm() # Tạo một biểu mẫu trống để hiển thị trên trang web
    return render(request, 'students/add_student.html', {'form': form}) # Truyền biểu mẫu vào ngữ cảnh để hiển thị trong template

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id) # Lấy đối tượng Student theo ID hoặc trả về lỗi 404 nếu không tìm thấy
    return render(request, 'students/student_detail.html', {'student': student})

# Hàm xử lý chỉnh sửa thông tin học sinh
def edit_student(request, student_id): # 
    student = get_object_or_404(Student, id=student_id) # Lấy đối tượng Student theo ID hoặc trả về lỗi 404 nếu không tìm thấy
    if request.method == 'POST': # Nếu biểu mẫu được gửi đi
        form = StudentForm(request.POST, instance=student) # instance=student để cập nhật đối tượng hiện có
        if form.is_valid(): # Kiểm tra tính hợp lệ của dữ liệu biểu mẫu
            form.save()
            return redirect('student_list') # Chuyển hướng về danh sách học sinh sau khi lưu
    else: # Nếu yêu cầu là GET, hiển thị biểu mẫu với dữ liệu hiện có
        form = StudentForm(instance=student) # Tạo biểu mẫu với dữ liệu hiện có của học sinh
    return render(request, 'students/edit_student.html', {'form': form, 'student': student}) # Truyền biểu mẫu và đối tượng học sinh vào ngữ cảnh để hiển thị trong template

def delete_student(request, student_id):
        student = get_object_or_404(Student, id=student_id)
#    if request.method == 'POST': # Nếu biểu mẫu được gửi đi (theo phương thức POST) thì xóa học sinh và chuyển hướng về danh sách học sinh sau khi xóa
        request.session['delete_student'] = { 
            'id': student.id,
            'name': student.name,
            'classroom': student.classroom,
            'gender': student.gender,
            'status': student.status,
            'score': student.score,
        }
        student.delete()
        messages.success(request, 'Học sinh đã được xóa thành công.')
        return redirect('student_list')

#    return render(request, 'students/delete_student.html', {'student': student})
    
def dashboard(request):
    total_students = Student.objects.count()
    avg_score = Student.objects.aggregate(Avg('score'))['score__avg'] # Tính điểm trung bình của tất cả học sinh
    return render(request, 'students/dashboard.html', { # Truyền dữ liệu vào ngữ cảnh để hiển thị trong template
        'total_students': total_students,
        'avg_score': avg_score
    })

