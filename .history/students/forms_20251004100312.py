from django import forms
from .models import Student

class StudentForm(forms.ModelForm): # Tạo một biểu mẫu dựa trên mô hình Student
    class Meta:
        model = Student  # Chỉ định mô hình mà biểu mẫu sẽ dựa trên
        fields = ['name', 'age', 'classroom', 'score', 'email', 'birthday']  # Các trường sẽ được bao gồm trong biểu mẫu
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})  # Sử dụng widget DateInput để chọn ngày
            
        }