from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Avg    
from django.contrib import messages 
from datetime import datetime
from django.views.decorators.http import require_POST


# Create your views here.

def home(request):
    return render(request, 'students/home.html')

def student_list(request): 
    classroom = request.GET.get('classroom') # Lấy giá trị của tham số 'classroom' từ URL (nếu có)
    gender = request.GET.get('gender') # Lấy giá trị của tham số 'gender' từ URL (nếu có)
    status = request.GET.get('status') # Lấy giá trị của tham số 'status' từ URL (nếu có) 
    students = Student.objects.all() # Lấy tất cả đối tượng Student từ cơ sở dữ liệu
    deleted_student = request.session.get('deleted_student')  # ❌ không xoá khỏi session để hiển thị trong template 

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
        'deleted_student': deleted_student,  # Truyền thông tin học sinh đã xóa vào ngữ cảnh để hiển thị trong template
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

    # Lưu thông tin vào session để có thể khôi phục lại nếu cần (undo), session là một dict lưu trữ dữ liệu tạm thời cho từng người dùng
    request.session['deleted_student'] = { # Lưu thông tin học sinh đã xoá vào session 
        'name': student.name,  # Lưu tất cả các trường cần thiết để khôi phục
        'age': student.age,
        'classroom': student.classroom,
        'gender': student.gender,
        'status': student.status,
        'score': student.score,
        'email': student.email,
        'birthday': str(student.birthday),  # chuyển về chuỗi để lưu vào session 
    }

    student.delete()
    messages.success(request, f'Đã xoá học sinh {student.name}')
    return redirect('student_list')

#    return render(request, 'students/delete_student.html', {'student': student})

@require_POST  # Chỉ cho phép phương thức POST gọi hàm này
def undo_delete(request):  #
    data = request.session.get('deleted_student') # Lấy dữ liệu học sinh đã xoá từ session 

    if not data: # Nếu không có dữ liệu trong session, hiển thị thông báo lỗi và chuyển hướng về danh sách học sinh
        messages.error(request, 'Không tìm thấy dữ liệu học sinh để khôi phục.')
        return redirect('student_list') 

    try: # Thử khôi phục học sinh từ dữ liệu trong session
        # Chuyển đổi dữ liệu ngày tháng từ chuỗi sang đối tượng date
        # Chuyển birthday từ chuỗi sang kiểu ngày
        birthday_str = data.get('birthday') # Lấy chuỗi ngày tháng từ dữ liệu
        # Chuyển đổi chuỗi sang đối tượng date, kiểm tra nếu không phải 'None' trước khi chuyển đổi 
        if birthday_str and birthday_str != 'None':
            data['birthday'] = datetime.strptime(birthday_str, '%Y-%m-%d').date() # Chuyển đổi chuỗi sang đối tượng date 
        else:
            data['birthday'] = None  # hoặc dùng ngày mặc định nếu cần

        # Tạo lại học sinh
        Student.objects.create(
            name=data.get('name'), # Lưu tên học sinh 
            age=data.get('age'), 
            classroom=data.get('classroom'),
            gender=data.get('gender'),
            status=data.get('status'),
            score=data.get('score'),
            email=data.get('email'),
            birthday=data.get('birthday')
        )

        # Xoá dữ liệu khỏi session
        request.session.pop('deleted_student', None) # Xoá khỏi session sau khi khôi phục thành công
         # Hiển thị thông báo thành công
        messages.success(request, f'Đã khôi phục học sinh {data.get("name")} thành công.')

    except Exception as e:
        messages.error(request, f'Lỗi khi khôi phục: {str(e)}')

    return redirect('student_list')
def dashboard(request):
    total_students = Student.objects.count()
    avg_score = Student.objects.aggregate(Avg('score'))['score__avg'] # Tính điểm trung bình của tất cả học sinh
    return render(request, 'students/dashboard.html', { # Truyền dữ liệu vào ngữ cảnh để hiển thị trong template
        'total_students': total_students,
        'avg_score': avg_score
    })

