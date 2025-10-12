from django import forms
from .models import Student, StudentNew

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class StudentFormClean(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    
class StudentFormNew(forms.ModelForm):
    class Meta:
        model = StudentNew
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'classroom': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'academic': forms.Select(attrs={'class': 'form-select'}),
            'study_status': forms.Select(attrs={'class': 'form-select'}),
            'application_status': forms.Select(attrs={'class': 'form-select'}),
            'application_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'application_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'payment_status': forms.Select(attrs={'class': 'form-select'}),
            'payment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
