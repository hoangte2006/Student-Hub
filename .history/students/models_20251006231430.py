from django.db import models
from django.views.generic import DetailView


class Student(models.Model): # ( ) đây là cách kế thừa từ lớp DJango, Model để tạo mô hình dữ liệu

    GENDER_CHOICES = [
        ('M', "Nam"),
        ('F', "Nữ"),
        ('O', "Khác"),
    ]

    GENDER_LABELS = {
        'M': 'Nam',
        'F': 'Nữ',
        'O': 'Khác',
    }

    ACADEMIC_LABELS = {
        'G': 'Giỏi',
        'K': 'Khá',
        'TB': 'Trung bình',
        'Y': 'Yếu',
    }

    ACADEMIC_CHOICES = [
        ('G', 'Giỏi'),
        ('K', 'Khá'),
        ('TB', 'Trung bình'),
        ('Y', 'Yếu'),
    ]

    STATUS_CHOICES = [
        ('A', 'Đang học'),
        ('N', 'Nghỉ học'),
        ('G', 'Đã tốt nghiệp'),
    ]

#Tham số	Ý nghĩa	Ví dụ
#max_length	Độ dài tối đa (bắt buộc với CharField)	max_length=50
#choices	Danh sách lựa chọn (hiển thị dropdown)	choices=GENDER_CHOICES
#default	Giá trị mặc định	default='M'
#null	Cho phép để trống trong database	null=True
#blank	Cho phép để trống trong form	blank=True
#unique	Không được trùng lặp	unique=True
#verbose_name	Tên hiển thị dễ hiểu	verbose_name='Họ tên'

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='G')
    academic = models.CharField(max_length=3, choices=ACADEMIC_CHOICES, default='TB')
    score = models.FloatField()
    email = models.EmailField(blank=True, null=True)         
    birthday = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)  # Trường để đánh dấu học sinh đã bị xoá

    def __str__(self):
        return f"{self.name} - {self.classroom}"
    
    def save(self, *args, **kwargs):
        if self.score is not None:
            if self.score >= 8:
                self.academic = 'G'
            elif self.score >= 6.5:
                self.academic = 'K'
            elif self.score >= 5:
                self.academic = 'TB'
            else:
                self.academic = 'Y'
        super().save(*args, **kwargs)

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
