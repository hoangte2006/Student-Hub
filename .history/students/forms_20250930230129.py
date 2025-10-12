from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'classroom', 'score', 'email', 'birthday']  # Thêm 'email' và 'birthday' vào danh sách trường cần hiển thị trong biểu mẫu
