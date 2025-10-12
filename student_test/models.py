from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', "Nam"),
        ('F', "Nữ"),
        ('O', "Khác"),
    ]

    ACADEMIC_CHOICES = [
        ('G', 'Giỏi'),
        ('K', 'Khá'),
        ('TB', 'Trung bình'),
        ('Y', 'Yếu'),   
    ]

    STATUS_CHOICES = [
        ('A', 'Đang học'),
        ('N', 'Nghỉ học'),
        ('S', 'Đã tốt nghiệp'),
    ]

    APPLICATION_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối'),
    ]

    PAYMENT_CHOICES = [
        ('paid', 'Đã đóng'),
        ('unpaid', 'Chưa đóng'),
        ('partial', 'Đóng một phần'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    study_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    academic = models.CharField(max_length=3, choices=ACADEMIC_CHOICES, default='TB')
    score = models.FloatField()
    email = models.EmailField(blank=True, null=True)         
    birthday = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)  

    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    application_date = models.DateField(null=True, blank=True)
    application_note = models.TextField(default="Không có ghi chú", blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_note = models.TextField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    application_status = models.CharField(max_length=10, choices=APPLICATION_CHOICES, default='pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='unpaid')

    def __str__(self):
        return f"{self.name} - {self.classroom}"
