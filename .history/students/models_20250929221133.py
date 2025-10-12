from django.db import models

class Student(models.Model): # ( ) đây là cách kế thừa lớp DJagon
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.CharField(max_length=20)
    score = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.classroom}"
