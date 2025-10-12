from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'classroom', 'gender', 'status', 'score', 'email', 'birthday']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),  # 👈 thêm dòng này
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
