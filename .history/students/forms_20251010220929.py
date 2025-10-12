from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class StudentFormFull(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
