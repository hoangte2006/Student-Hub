from django.db import models

class Student(models.Model): # ( ) đây là cách kế thừa từ lớp DJango, Model để tạo mô hình dữ liệu

    GENDER_CHOICES = [
        ('M', "Nam"),
        ('F', "Nữ"),
        ('O', "Khác"),
    ]

    STATUS_CHOICES = [ 
        ('G', 'Tốt'),
        ('K', 'Khá'),
        ('T', 'Trung bình'),
        ('Y', 'Yếu'),
    ]


    def __str__(self):
        return f"{self.name} - {self.classroom}"
