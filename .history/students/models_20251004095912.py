from django.db import models

class Student(models.Model): # ( ) đây là cách kế thừa từ lớp DJango
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.CharField(max_length=20)
    score = models.FloatField()
    email = models.EmailField(blank=True, null=True)         
    birthday = models.DateField(blank=True, null=True)       

    GENDER_CHOICES = [
        ('M'm "")
    ]

    def __str__(self):
        return f"{self.name} - {self.classroom}"
