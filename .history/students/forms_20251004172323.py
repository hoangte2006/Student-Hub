from django import forms
from .models import Student

class StudentForm(forms.ModelForm): # Tạo một biểu mẫu dựa trên mô hình Student
    class Meta:
        model = Student  # Chỉ định mô hình mà biểu mẫu sẽ dựa trên
        fields = ['name', 'age', 'classroom', 'score', 'email', 'birthday', 'gender', 'status']  # Các trường sẽ được bao gồm trong biểu mẫu
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),  # Sử dụng widget DateInput để chọn ngày
            'gender': forms.Select(attrs={'class': 'form-select'}), # Thêm class CSS cho trường giới tính 
            'status': forms.Select(attrs={'class': 'form-select'}), # Thêm class CSS cho trường trạng thái
        }