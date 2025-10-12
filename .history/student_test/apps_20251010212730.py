from django.apps import AppConfig


class StudentTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_test'
from django.apps import AppConfig

class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
