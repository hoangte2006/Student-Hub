from django import forms
from .models import Student

class StudentForm(forms.ModelForm): # Tạo một biểu mẫu dựa trên mô hình Student
    class Meta: 
        # Đây là lớp con đặc biệt nằm trong StudentForm
        # Django dùng nó để biết: “Form này liên kết với model nào, và gồm những trường nào?”
        model = Student # là mô hình dữ liệu mà biểu mẫu sẽ tương tác với bảng Student trong cơ sở dữ liệu

        fields = ['name', 'age', 'classroom', 'gender', 'study_status', 'academic', 'score', 'email', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
#            'classroom': forms.TextInput(attrs={'class': 'form-control'}),
#            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
#            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
#            'gender': forms.Select(attrs={'class': 'form-select'}),
#            'status': forms.Select(attrs={'class': 'form-select'}),
        }
