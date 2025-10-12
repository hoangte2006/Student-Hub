from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'gender': forms.Select(choices=Student.GENDER_CHOICES, attrs={'class': 'form-select'}),
            'study_status': forms.Select(choices=Student.STATUS_CHOICES, attrs={'class': 'form-select'}),
            'academic': forms.Select(choices=Student.ACADEMIC_CHOICES, attrs={'class': 'form-select'}),
            'application_status': forms.Select(choices=Student.APPLICATION_CHOICES, attrs={'class': 'form-select'}),
            'payment_status': forms.Select(choices=Student.PAYMENT_CHOICES, attrs={'class': 'form-select'}),

            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'application_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'classroom': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'application_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'payment_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
